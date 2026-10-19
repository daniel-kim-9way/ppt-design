# 디자인 시스템 명세(getdesign.md) → 테마 변환

사용자가 **getdesign.md 형식의 디자인 시스템 마크다운**(getdesign.md / `/preview-design`
스타일, `{colors.*}` `{typography.*}` `{rounded.*}` 토큰을 쓰는 문서)을 붙여넣으면,
그 내용을 읽어 **PPT Design 테마 JSON**으로 변환한다. 이후 그 테마로 덱을 만든다.

> 받는 곳: 무료 모음 https://github.com/VoltAgent/awesome-design-md (`design-md/<사이트>/DESIGN.md`) ·
> 더 많은 목록 https://getdesign.md/design-md (일부는 유료 Catalog Pass이거나 로그인이 필요하다).
> DESIGN.md는 맨 위 YAML에 `colors:`(primary · canvas · surface-card · ink · hairline …)와
> `typography:`(fontFamily · fontSize · fontWeight …)를 담는다. 아래 표의 `{colors.primary}`는
> 그 YAML의 `colors.primary` 값을 뜻한다. 이 스킬은 그 값을 받아 PPTX 테마로 재현한다.

## 절차
1. 명세에서 **canvas 색의 밝기**로 라이트/다크를 판별한다(near-black이면 `mode:"dark"`).
2. 명세의 `{colors.*}`를 아래 표대로 PPT Design 슬롯에 매핑한다.
   명세에 없는 슬롯은 `theme.build_palette[_dark]`의 파생 규칙대로 채우거나
   가장 가까운 값을 쓴다.
3. 폰트: 본문/디스플레이 = 명세의 sans, mono = 명세의 mono. 굵기별 패밀리가
   명시돼 있으면 `weights`에 넣는다.
4. 명세 글꼴이 Inter·Geist처럼 **한글이 없는 영문 글꼴이면** `fonts.ko`를 `"Pretendard"`로 둔다
   (영문은 명세 글꼴, 한글은 Pretendard). 한글 덱이면 빠뜨리지 않는다.
5. `theme.json`을 `OUTPUT/ppt-design/<프로젝트>/theme.json`에 저장하고 `Deck(theme=...)`로 쓴다.

## 색 슬롯 매핑 (getdesign.md → PPT Design)
| PPT Design 슬롯 | 라이트 명세 출처 | 다크 명세 출처 |
|---|---|---|
| `primary` | `{colors.primary}` | `{colors.primary}` |
| `primary_active` | primary 진한 변형 / `primary-deep` | 〃 |
| `primary_disabled` | primary↔canvas 혼합 / `primary-disabled` | 〃 |
| `accent_teal` / `accent_amber` | 보조 액센트 2,3 (없으면 primary 변형) | 단일 액센트면 primary 톤 변형 |
| `canvas` | `{colors.canvas}`(밝음) | `{colors.canvas}`(near-black) |
| `surface_soft` | canvas 살짝 변형 / `surface-soft` | `canvas-soft` |
| `surface_card` | 카드 배경 / `surface-card` | **= canvas** (hairline 카드용) |
| `surface_cream_strong` | 강조 밴드 surface | canvas 살짝 밝게 |
| `surface_dark` | 다크 강조 surface | 가장 어두운(거의 검정) |
| `surface_dark_elevated/soft` | 다크 변형 | canvas 살짝 밝게 |
| `hairline` | `{colors.hairline}` | `{colors.hairline}` |
| `ink` | 본문 1차 글자 | `{colors.ink}`(밝은 off-white) |
| `body_strong` | 강조 글자 / `ink-strong` | `ink-strong`(흰색) |
| `body` | 본문 2차 | `{colors.body}` |
| `muted` / `muted_soft` | 캡션/뮤트 | `{colors.mute}` 등 |
| `on_primary` | primary 위 글자(보통 흰/검 자동) | 〃 |
| `on_dark` / `on_dark_soft` | 다크 위 글자 | ink / body |
| `success/warning/error` | semantic (없으면 primary/기본) | 〃 |

## 다크 모드 처리 (중요)
명세가 **다크 캔버스 전용**(Voltagent처럼 #101010 + 단일 액센트)이면:
- `mode: "dark"` 로 둔다 → 카드가 **자동으로 hairline 보더**를 갖는다
  (`surface_card == canvas` + 1px hairline = 브랜드의 카드 시그니처).
- 모든 글자 슬롯은 밝게, 모든 surface는 어둡게.
- `surface_dark`는 캔버스보다 더 어둡게(거의 검정)해 강조 밴드가 미세 대비를 갖게.
- 단일 액센트 브랜드는 `accent_teal/accent_amber`도 주색 톤 변형으로(과한 색 추가 금지).

## 시드로 빠르게 만들기
명세의 핵심 색만 뽑아 파생해도 된다.
```python
import theme as th
# 라이트 브랜드
t = th.from_seeds(font="Inter", primary="#...", canvas="#FFFFFF",
                  ink="#0F172A", dark="#0B1220", mode="light", name="brand",
                  ko="Pretendard")          # Inter엔 한글이 없어서 한글은 Pretendard
# 다크 브랜드 (Voltagent류) — dark 생략, canvas가 near-black
t = th.from_seeds(font="Inter", primary="#00D992", canvas="#101010",
                  ink="#F2F2F2", accent2="#2FD6A1", accent3="#10B981",
                  mode="dark", name="brand", ko="Pretendard")
th.save(t, "OUTPUT/ppt-design/brand/theme.json")
```
정확도를 높이려면 명세에 적힌 정확한 hex(hairline, body, muted 등)를 생성된 dict에
덮어쓴다.

## 폰트
- 본문/디스플레이 = 명세 sans(예: Inter), mono = 명세 mono(예: SF Mono).
- 한글 = `fonts.ko`(명세 글꼴에 한글이 없으면 `"Pretendard"`).
- 그 폰트가 **보는 PC에 설치돼 있어야** 동일하게 렌더된다(python-pptx는 임베드 불가).
  미설치 시 시스템 폰트로 폴백 — 색/레이아웃은 유지되지만 글꼴이 달라진다.
- SF Mono 등 OS 전용 폰트는 명세대로 두되, 대체 폰트(JetBrains/Geist/Cascadia Mono)를
  사용자에게 안내한다.

## 검증
변환 후 반드시 PNG로 렌더해 대비(특히 다크에서 글자 가독성)와 카드 보더를 확인한다.

## 프리셋 예시
`themes/voltagent-dark.json` — 위 Voltagent 명세를 그대로 옮긴 다크 프리셋(참고용).
