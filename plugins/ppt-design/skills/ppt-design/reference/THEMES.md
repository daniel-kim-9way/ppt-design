# 테마 가이드

테마 = **색 팔레트(26 슬롯) + 폰트**. 레이아웃은 의미 슬롯 이름만 참조하므로,
테마만 바꾸면 같은 코드가 다른 스타일로 렌더된다.

## 적용 방법
```python
Deck(theme="cream-coral")                  # 프리셋 이름
Deck(theme="OUTPUT/acme/theme.json")       # 파일
Deck(theme={...})                          # dict
# theme 생략 시 기본 cream-coral
```

## 프리셋
| 이름 | 모드 | 설명 |
|---|---|---|
| `cream-coral` | light | Anthropic/Claude 스타일. 크림 + 코랄 + 다크 네이비 (기본) |
| `slate-blue` | light | 기업/IT 제안·보고용. 슬레이트 블루 + 화이트 |
| `ink-mono` | light | 미니멀 모노톤. 잉크 블랙 + 그레이 |
| `voltagent-dark` | **dark** | Voltagent 스타일. near-black + 일렉트릭 그린. hairline 카드 |

## 라이트 / 다크 모드
- `mode: "light"`(기본) — 밝은 캔버스. 카드는 채워진 surface.
- `mode: "dark"` — near-black 캔버스 + 밝은 글자. **카드가 자동으로 hairline 보더**를
  갖는다(`surface_card == canvas` + 1px hairline). `card_hairline: true/false`로 강제 지정 가능.
- 다크 브랜드는 `from_seeds(..., mode="dark")`(시드: primary·canvas·ink·accent2·accent3,
  dark 생략) 또는 명세 변환(`reference/DESIGN-MD.md`)으로 만든다.

## 사용자 스타일로 테마 만들기 (first-use)
폰트 + 시드 색 몇 개만 주면 전체 팔레트를 파생한다.
```python
import theme as th
t = th.from_seeds(
    font="Pretendard",       # 본문/디스플레이 폰트 (설치돼 있어야 함)
    primary="#2563EB",       # 주색: CTA·강조·콜아웃
    canvas="#FFFFFF",        # 페이지 배경
    ink="#0F172A",           # 본문 글자색
    dark="#0B1220",          # 다크 서피스(섹션·포스터·푸터 대비)
    accent2="#0EA5E9",       # 보조 강조 1 (생략 시 자동)
    accent3="#F59E0B",       # 보조 강조 2 (생략 시 자동)
    mono="Consolas",         # 코드용 (생략 가능)
    weights={                # 굵기별 폰트 패밀리 (있을 때만)
        "Light":"Pretendard Light","SemiBold":"Pretendard SemiBold",
        "ExtraBold":"Pretendard ExtraBold","Black":"Pretendard Black"},
    name="acme")
th.save(t, "OUTPUT/acme/theme.json")
```

### 파생 규칙 (시드 → 26 슬롯)
- `primary_active` = primary 22% 어둡게 · `primary_disabled` = primary↔canvas 혼합
- `surface_soft/card/cream_strong` = canvas 3/6/10% 어둡게 · `hairline` = 8% 어둡게
- `surface_dark_elevated/soft` = dark 살짝 밝게
- `body_strong/body/muted/muted_soft` = ink 점점 밝게
- `on_primary` = primary 명도로 흰/검 자동 · `on_dark` = canvas톤 · `on_dark_soft` = canvas↔dark 혼합
- `success/warning/error` = 기본값(인자로 교체 가능)

## 색 슬롯 전체 목록 (직접 dict로 만들 때 필수)
```
primary primary_active primary_disabled
accent_teal accent_amber
canvas surface_soft surface_card surface_cream_strong
surface_dark surface_dark_elevated surface_dark_soft
hairline hairline_soft
ink body_strong body muted muted_soft
on_primary on_dark on_dark_soft
success warning error
```

## 폰트
- `fonts.body` / `fonts.display` — 디스플레이가 본문과 다르면 display 토큰만 그 폰트 사용
  (예: 세리프 디스플레이 + 산세리프 본문). 같게 두면 단일 폰트.
- `fonts.weights` — 굵기별 전용 패밀리명(예: "Pretendard Light"). 없으면 본문 폰트 +
  bold 근사(Thin/Light 같은 미세 굵기는 Regular로 보임).
- `fonts.ko` / `fonts.ko_weights` — **한글 글꼴.** 본문 글꼴이 Inter처럼 한글이 없는 영문 글꼴이면
  `"ko": "Pretendard"`를 준다. 그러면 영문은 본문 글꼴, 한글은 Pretendard로 그린다.
  안 주면 한글이 PC마다 다른 글꼴로 대신 그려져 한 문장 안에서 굵기가 섞여 보인다.
  `from_seeds(..., ko="Pretendard")`로도 줄 수 있다. 다크 프리셋 `voltagent-dark`가 이렇게 돼 있다.
- python-pptx는 폰트를 파일에 임베드하지 못한다 → 보는 PC에 폰트 설치 필요.

## 색 대비 주의
- `canvas`는 밝게, `ink`는 충분히 어둡게(대비). `dark`는 충분히 어둡게.
- 어두운 캔버스 테마는 `mode: "dark"`로 만든다(위 «라이트 / 다크 모드»).
- 강조색(primary)이 어두운 서피스와 비슷하면(ink-mono처럼 강조색이 검정), 어두운 장의
  강조 글자·버튼은 자동으로 밝은 글자색(on_dark)으로 바뀐다.
