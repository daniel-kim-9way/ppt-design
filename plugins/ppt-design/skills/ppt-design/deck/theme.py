# -*- coding: utf-8 -*-
"""
테마 시스템 — 폰트 + 디자인 스타일(색)을 정의하고 적용한다.

핵심:
  theme.use("cream-coral")              # 프리셋 이름
  theme.use("path/to/my-theme.json")    # 파일
  theme.use({...})                       # dict
  t = theme.from_seeds(font="Inter", primary="#2563EB", canvas="#FFFFFF",
                       ink="#0F172A", dark="#0B1220")   # 시드 몇 개 → 전체 팔레트
  theme.save(t, "OUTPUT/<proj>/theme.json")
"""
import json
import os

THEMES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "themes")


# ---------------------------------------------------------------------------
# 색 유틸 (순수 파이썬, 의존성 없음)
# ---------------------------------------------------------------------------
def _h2r(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def _r2h(r):
    return "{:02X}{:02X}{:02X}".format(*(max(0, min(255, int(round(v)))) for v in r))


def _mix(c1, c2, t):
    a, b = _h2r(c1), _h2r(c2)
    return _r2h(tuple(a[i] + (b[i] - a[i]) * t for i in range(3)))


def lighten(c, t):
    return _mix(c, "#FFFFFF", t)


def darken(c, t):
    return _mix(c, "#000000", t)


def _luma(c):
    r, g, b = _h2r(c)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def on(c):
    """배경 c 위에 올릴 글자색(흰/검) 자동 선택."""
    return "#FFFFFF" if _luma(c) < 0.6 else "#141413"


# ---------------------------------------------------------------------------
# 시드 → 전체 팔레트 파생
# ---------------------------------------------------------------------------
def build_palette(primary, canvas, ink, dark,
                  accent2=None, accent3=None,
                  success="#5DB872", warning="#D4A017", error="#C64545"):
    """소수의 시드 색에서 26개 의미 슬롯을 파생."""
    accent2 = accent2 or _mix(primary, "#3CB39E", 0.5)
    accent3 = accent3 or _mix(primary, "#E8A55A", 0.5)
    p = {
        "primary": primary.lstrip("#"),
        "primary_active": darken(primary, 0.22),
        "primary_disabled": _mix(primary, canvas, 0.72),
        "accent_teal": accent2.lstrip("#"),
        "accent_amber": accent3.lstrip("#"),
        "canvas": canvas.lstrip("#"),
        "surface_soft": darken(canvas, 0.03),
        "surface_card": darken(canvas, 0.06),
        "surface_cream_strong": darken(canvas, 0.10),
        "surface_dark": dark.lstrip("#"),
        "surface_dark_elevated": lighten(dark, 0.07),
        "surface_dark_soft": lighten(dark, 0.035),
        "hairline": darken(canvas, 0.08),
        "hairline_soft": darken(canvas, 0.05),
        "ink": ink.lstrip("#"),
        "body_strong": lighten(ink, 0.08),
        "body": lighten(ink, 0.20),
        "muted": lighten(ink, 0.46),
        "muted_soft": lighten(ink, 0.58),
        "on_primary": on(primary).lstrip("#"),
        "on_dark": lighten(canvas, 0.0),
        "on_dark_soft": _mix(canvas, dark, 0.5),
        "success": success.lstrip("#"),
        "warning": warning.lstrip("#"),
        "error": error.lstrip("#"),
    }
    return {k: v.lstrip("#") for k, v in p.items()}


def build_palette_dark(primary, canvas, ink, accent2=None, accent3=None,
                       hairline=None,
                       success=None, warning="D4A017", error="C64545"):
    """다크 브랜드(near-black 캔버스 + 밝은 글자)용 파생.
    canvas=어두운 배경, ink=밝은 off-white."""
    accent2 = accent2 or primary
    accent3 = accent3 or primary
    success = success or primary       # 다크 브랜드는 보통 주색을 success로
    return {k: v.lstrip("#") for k, v in {
        "primary": primary, "primary_active": darken(primary, 0.18),
        "primary_disabled": _mix(primary, canvas, 0.72),
        "accent_teal": accent2, "accent_amber": accent3,
        "canvas": canvas,
        "surface_soft": lighten(canvas, 0.04),
        "surface_card": canvas,                       # hairline 카드(보더로 구분)
        "surface_cream_strong": lighten(canvas, 0.09),
        "surface_dark": darken(canvas, 0.5),          # 가장 어두운 강조 밴드
        "surface_dark_elevated": lighten(canvas, 0.06),
        "surface_dark_soft": lighten(canvas, 0.03),
        "hairline": hairline or lighten(canvas, 0.18),
        "hairline_soft": lighten(canvas, 0.30),
        "ink": ink, "body_strong": "#FFFFFF",
        "body": darken(ink, 0.22), "muted": darken(ink, 0.42),
        "muted_soft": darken(ink, 0.52),
        "on_primary": on(primary), "on_dark": ink, "on_dark_soft": darken(ink, 0.22),
        "success": success, "warning": warning, "error": error,
    }.items()}


def from_seeds(font, primary, canvas, ink, dark=None, accent2=None, accent3=None,
               mono="Consolas", display=None, weights=None, name="custom",
               mode="light", ko=None, ko_weights=None):
    """폰트 + 시드 색 → 완성된 테마 dict.
    mode='light': dark(다크 서피스 시드) 필요. mode='dark': near-black 브랜드(dark 생략).
    weights: {굵기명: 패밀리} (Pretendard처럼 굵기별 패밀리가 있으면 지정).
    ko: 한글 글꼴. font 가 Inter처럼 한글이 없는 글꼴이면 "Pretendard" 를 준다.
    ko_weights: 한글 글꼴의 굵기별 패밀리(있을 때만)."""
    if mode == "dark":
        colors = build_palette_dark(primary, canvas, ink, accent2, accent3)
    else:
        colors = build_palette(primary, canvas, ink, dark or "#181715",
                               accent2, accent3)
    t = {
        "name": name, "mode": mode, "colors": colors,
        "fonts": {"body": font, "display": display or font, "mono": mono,
                  "weights": weights or {}},
    }
    if ko:
        t["fonts"]["ko"] = ko
        if ko_weights:
            t["fonts"]["ko_weights"] = ko_weights
    return t


# ---------------------------------------------------------------------------
# 로드 / 적용 / 저장
# ---------------------------------------------------------------------------
def _resolve(theme):
    if isinstance(theme, dict):
        return theme
    if isinstance(theme, str):
        path = theme
        if not theme.lower().endswith(".json"):
            path = os.path.join(THEMES_DIR, theme + ".json")   # 프리셋 이름
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    raise TypeError("theme은 dict / 파일경로 / 프리셋이름")


def use(theme):
    """테마 적용. 이후 생성되는 모든 슬라이드에 반영."""
    import tokens as T
    t = _resolve(theme)
    T.apply(t["colors"], t["fonts"],
            mode=t.get("mode", "light"),
            card_hairline=t.get("card_hairline"))
    return t


def save(theme, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(theme, f, ensure_ascii=False, indent=2)
    return path


def list_presets():
    if not os.path.isdir(THEMES_DIR):
        return []
    return sorted(f[:-5] for f in os.listdir(THEMES_DIR) if f.endswith(".json"))
