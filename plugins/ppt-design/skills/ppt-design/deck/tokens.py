# -*- coding: utf-8 -*-
"""
디자인 토큰 — 스케일(테마 무관)과 '활성 테마'(색/폰트, 교체 가능)로 나뉜다.
theme.use(...)가 apply()를 호출해 COLORS / WEIGHT_MAP / FONT_* 를 갈아끼운다.
helpers/layouts는 호출 시점에 이 모듈 globals를 읽으므로 테마 전환이 즉시 반영된다.
"""

# ---------------------------------------------------------------------------
# 슬라이드 캔버스 (16:9, 1280x720 px)
# ---------------------------------------------------------------------------
SLIDE_W_PX = 1280
SLIDE_H_PX = 720

# ---------------------------------------------------------------------------
# 타이포 스케일 (테마 무관 · px 기준, 빌더가 pt = px*0.75 로 변환)
#   token: (size_px, weight, line_height, letter_spacing_px)
# ---------------------------------------------------------------------------
TYPE = {
    "display_xl":    (64, "Light",    1.05, -1.5),
    "display_lg":    (48, "Light",    1.10, -1.0),
    "display_md":    (36, "Regular",  1.15, -0.5),
    "display_sm":    (28, "Regular",  1.20, -0.3),
    "title_lg":      (22, "SemiBold", 1.30,  0.0),
    "title_md":      (18, "SemiBold", 1.40,  0.0),
    "title_sm":      (16, "SemiBold", 1.40,  0.0),
    "body_md":       (16, "Regular",  1.55,  0.0),
    "body_sm":       (14, "Regular",  1.55,  0.0),
    "caption":       (13, "Medium",   1.40,  0.0),
    "caption_upper": (12, "Medium",   1.40,  1.5),
    "code":          (14, "Regular",  1.60,  0.0),
    "button":        (14, "Medium",   1.00,  0.0),
    "nav_link":      (14, "Medium",   1.40,  0.0),
}

SPACING = {"xxs":4,"xs":8,"sm":12,"md":16,"lg":24,"xl":32,"xxl":48,"section":96}
RADIUS  = {"xs":4,"sm":6,"md":8,"lg":12,"xl":16,"pill":999,"full":999}

# 색 슬롯 — 모든 테마가 채워야 하는 의미 토큰 (레이아웃이 참조하는 이름)
COLOR_SLOTS = [
    "primary","primary_active","primary_disabled",
    "accent_teal","accent_amber",
    "canvas","surface_soft","surface_card","surface_cream_strong",
    "surface_dark","surface_dark_elevated","surface_dark_soft",
    "hairline","hairline_soft",
    "ink","body_strong","body","muted","muted_soft",
    "on_primary","on_dark","on_dark_soft",
    "success","warning","error",
]

# 굵기 순서 (WEIGHT_MAP 생성용)
WEIGHTS = ["Thin","ExtraLight","Light","Regular","Medium","SemiBold",
           "Bold","ExtraBold","Black"]
HEAVY = {"Bold","ExtraBold","Black"}

# ---------------------------------------------------------------------------
# 활성 테마 상태 (apply 로 교체됨)
# ---------------------------------------------------------------------------
COLORS = {}          # 슬롯명 -> hex
WEIGHT_MAP = {}      # 굵기명 -> (폰트 패밀리, bold flag)
FONT_BODY = "Pretendard"
FONT_DISPLAY = "Pretendard"
FONT_MONO = "Consolas"
FONT_KO = "Pretendard"   # 한글(ea) 글꼴. 테마 fonts.ko 가 없으면 본문 글꼴과 같다
KO_WEIGHT_MAP = {}   # 굵기명 -> 한글 글꼴 패밀리
MODE = "light"       # "light" | "dark"
CARD_HAIRLINE = False  # True면 surface_card 카드가 자동으로 hairline 보더를 가짐


def apply(palette, fonts, mode="light", card_hairline=None):
    """테마 적용. palette: 슬롯->hex dict,
    fonts: {body, display?, mono?, weights?, ko?, ko_weights?}.
    ko: 한글 글꼴. body 가 Inter처럼 한글이 없는 글꼴일 때 "Pretendard" 등을 준다.
    mode: 'light'|'dark'. card_hairline: None이면 dark일 때 자동 True."""
    global COLORS, WEIGHT_MAP, FONT_BODY, FONT_DISPLAY, FONT_MONO
    global FONT_KO, KO_WEIGHT_MAP, MODE, CARD_HAIRLINE
    MODE = mode
    CARD_HAIRLINE = (mode == "dark") if card_hairline is None else card_hairline
    missing = [s for s in COLOR_SLOTS if s not in palette]
    if missing:
        raise ValueError(f"테마 색 슬롯 누락: {missing}")
    COLORS = dict(palette)
    FONT_BODY = fonts["body"]
    FONT_DISPLAY = fonts.get("display", FONT_BODY)
    FONT_MONO = fonts.get("mono", "Consolas")
    wfam = fonts.get("weights", {})
    WEIGHT_MAP = {}
    for w in WEIGHTS:
        if w in wfam:                      # 굵기별 전용 패밀리가 있으면 그대로
            WEIGHT_MAP[w] = (wfam[w], False)
        else:                              # 없으면 본문 폰트 + bold 근사
            WEIGHT_MAP[w] = (FONT_BODY, w in HEAVY)
    # 한글 글꼴: ko 가 없으면 영문과 같은 패밀리(예전 동작). 있으면 한글만 따로.
    # 영문이 bold 근사로 굵기를 내면 한글도 기본 패밀리 + bold 로 맞춘다.
    ko = fonts.get("ko")
    kw = fonts.get("ko_weights", {})
    FONT_KO = ko or FONT_BODY
    KO_WEIGHT_MAP = {}
    for w in WEIGHTS:
        fam, bold = WEIGHT_MAP[w]
        if not ko:
            KO_WEIGHT_MAP[w] = fam
        else:
            KO_WEIGHT_MAP[w] = FONT_KO if bold else kw.get(w, FONT_KO)


# 기본 테마 (크림/코랄 + Pretendard) — 테마 미설정 시에도 동작하도록 import 시 적용
_DEFAULT_COLORS = {
    "primary":"CC785C","primary_active":"A9583E","primary_disabled":"E6DFD8",
    "accent_teal":"5DB8A6","accent_amber":"E8A55A",
    "canvas":"FAF9F5","surface_soft":"F5F0E8","surface_card":"EFE9DE",
    "surface_cream_strong":"E8E0D2","surface_dark":"181715",
    "surface_dark_elevated":"252320","surface_dark_soft":"1F1E1B",
    "hairline":"E6DFD8","hairline_soft":"EBE6DF",
    "ink":"141413","body_strong":"252523","body":"3D3D3A",
    "muted":"6C6A64","muted_soft":"8E8B82",
    "on_primary":"FFFFFF","on_dark":"FAF9F5","on_dark_soft":"A09D96",
    "success":"5DB872","warning":"D4A017","error":"C64545",
}
_DEFAULT_FONTS = {
    "body":"Pretendard","display":"Pretendard","mono":"Consolas",
    "weights":{"Thin":"Pretendard Thin","ExtraLight":"Pretendard ExtraLight",
               "Light":"Pretendard Light","Regular":"Pretendard",
               "Medium":"Pretendard Medium","SemiBold":"Pretendard SemiBold",
               "ExtraBold":"Pretendard ExtraBold","Black":"Pretendard Black"},
}
apply(_DEFAULT_COLORS, _DEFAULT_FONTS)
