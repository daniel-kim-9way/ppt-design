---
name: ppt-design
description: 발표자료(PPTX)를 디자인 시스템 기반으로 생성한다. 사용자가 폰트와 색/스타일을 주거나 DESIGN.md를 주면 그 테마로, 안 주면 기본(크림·코랄) 테마로 만든다. 제안서·보고서·강의·가이드북 등 덱 유형별 구성을 지원한다. 파라미터화된 레이아웃 58종으로 수정 가능한 .pptx를 만든다. "PPT/발표자료/강의안/제안서/보고서/가이드북 만들어줘", "이 스타일로 슬라이드", "우리 브랜드 색으로 덱", "DESIGN.md로 PPT" 등에 사용.
---

# PPT Design — 테마 가능한 PPTX 덱 생성기

디자인 시스템(색·폰트·레이아웃)을 코드로 정의해 일관된 `.pptx`를 찍어낸다.
**테마(폰트+스타일)는 교체 가능**하고, **덱 유형(제안서/보고서/강의/가이드북)**별로
구성을 다르게 가져간다. 하드코딩이 아니라 파라미터화된 레이아웃을 조합한다.

## 사전 요건
- Python 3 + `python-pptx`. 없으면 먼저 설치한다: `python -m pip install python-pptx`
  (Windows에서 `python`이 없으면 `py -m pip install python-pptx`). Pillow는 같이 설치된다.
- 테마 폰트. 기본 테마는 Pretendard(https://github.com/orioncactus/pretendard).
  없어도 만들어지지만, 보는 PC에서 다른 글꼴로 대신 그려진다.
- 렌더 검증(선택): PowerPoint(Windows) 또는 LibreOffice

## 라이브러리 위치
라이브러리는 이 스킬 폴더의 `deck/`에 있다: `${CLAUDE_SKILL_DIR}/deck`
- `builder.py` — `Deck(theme=..., kind=...)`, `save_project()`
- `layouts.py` — 레이아웃 58종 → **`reference/LAYOUTS.md`**
- `theme.py` — 테마 로드/생성/적용 → **`reference/THEMES.md`**
- `decktypes.py` — 유형별 추천 구성 → **`reference/DECK-TYPES.md`**
- 디자인 명세(DESIGN.md) → 테마 변환 → **`reference/DESIGN-MD.md`**
- `themes/*.json` — 프리셋(cream-coral, slate-blue, ink-mono, voltagent-dark)
- `tokens.py` / `helpers.py` — 스케일·저수준 드로잉

## 워크플로

### 1) 덱 프리셋 확인하기 (첫 사용 시 우선)
처음 쓰는 사용자에게는 바로 슬라이드를 만들기 전에 **덱 스타일**을 먼저 확인한다.
가장 권하는 방법은 잘 알려진 사이트의 `DESIGN.md`(색·글꼴·여백을 정리한 문서)를 받아 덱 프리셋으로 쓰는 것이다.
- 무료 모음: https://github.com/VoltAgent/awesome-design-md — `design-md/<사이트>/DESIGN.md`를 그대로 받는다.
- 더 많은 목록: https://getdesign.md/design-md — 일부는 유료(Catalog Pass)이거나 로그인이 필요하다.

사용자가 아직 스타일을 정하지 않았다면 이렇게 안내한다:
```text
먼저 원하는 사이트 스타일의 DESIGN.md를 하나 골라 덱 프리셋으로 쓰는 것을 권해요.
무료 모음: https://github.com/VoltAgent/awesome-design-md
받은 DESIGN.md를 프로젝트 폴더에 두면 그 색·글꼴·여백으로 PPT를 만들어요.
바로 시작하려면 기본 cream-coral 테마로 만들 수도 있어요.
```

이미 `DESIGN.md`가 프로젝트에 있거나 사용자가 붙여넣었다면, 그 명세를 먼저 읽고
`reference/DESIGN-MD.md`의 매핑대로 테마로 변환한다. 이후 생성되는 덱은 이 테마를 기본값으로 삼는다.

### 2) 유형 + 테마 정하기
사용자에게 두 가지를 확인한다(이미 말했으면 생략):
- **덱 유형**: 제안서 / 보고서 / 강의 / 가이드북 (`proposal|report|lecture|guidebook`)
- **디자인 테마**:
  - (a) **DESIGN.md 사용**: 첫 사용 시 가장 권장. `colors`·`typography` 토큰을 읽어 테마로 변환한다.
  - (b) 프리셋 사용: `cream-coral`(기본) / `slate-blue` / `ink-mono` / `voltagent-dark`(다크)
  - (c) **사용자 스타일 제공**: 폰트명 + 핵심 색 몇 개(주색·배경·글자색·다크색)
    또는 참고 이미지/URL의 색. → `theme.from_seeds(...)`로 전체 팔레트 자동 생성.
  - near-black 캔버스면 `mode:"dark"`(카드 자동 hairline).

### 3) (사용자 스타일일 때) 테마 파일 생성
```python
import theme as th
t = th.from_seeds(
    font="Pretendard",          # 설치된 폰트명
    primary="#2563EB",          # 주색(CTA·강조)
    canvas="#FFFFFF",           # 배경
    ink="#0F172A",              # 본문 글자
    dark="#0B1220",             # 다크 서피스
    accent2="#0EA5E9", accent3="#F59E0B",   # 보조 강조(생략 가능)
    name="acme")
th.save(t, "OUTPUT/ppt-design/<프로젝트>/theme.json")   # 프로젝트에 함께 저장
```
시드 4~6색에서 26개 의미 슬롯(surface/hairline/muted/on_dark 등)을 자동 파생한다.
굵기별 폰트 패밀리가 있으면 `weights={...}`로 지정(없으면 bold로 근사).
**글꼴이 Inter처럼 한글이 없는 영문 글꼴이면 `ko="Pretendard"`를 함께 준다.** 안 주면 한글이
PC마다 다른 글꼴로 대신 그려져 한 문장 안에서 굵기가 섞여 보인다.

### 4) 슬라이드 기획 (유형 흐름 참고)
`decktypes.flow("<유형>")`의 추천 구성을 참고해 슬라이드 리스트를 짠다.
같은 레이아웃을 3장 이상 연속 쓰지 않는다. 다크/포스터로 리듬을 준다.
사진·스크린샷이 있으면 사진 레이아웃(`cover_photo`·`photo_hero`·`shots_row` 등)을 쓴다.

### 5) 빌드 스크립트 작성 → `OUTPUT/ppt-design/<프로젝트>/build.py`
```python
import sys
sys.path.insert(0, r"${CLAUDE_SKILL_DIR}/deck")
from builder import Deck
import layouts as L

PROJECT = "acme-proposal"
d = Deck(theme="slate-blue", kind="proposal", brand="ACME · 제안서")
#   theme=프리셋이름 | "OUTPUT/ppt-design/acme-proposal/theme.json" | dict
L.cover(d, title="...", title2="...", subtitle="...", brand="ACME")
L.stat_cards(d, "...", [("…","…","…"), ...])
# ... 유형 흐름대로 레이아웃 조합 ...
print(d.save_project(PROJECT, "ACME_Proposal.pptx"))
```
`sys.path`에는 위 경로를 그대로 쓴다(이 스킬이 설치된 실제 폴더로 바뀌어 보인다).

### 6) 실행 & 검증
작업 폴더에서 `python OUTPUT/ppt-design/<프로젝트>/build.py`를 실행한다.
그림으로 뽑아 Read로 확인하고, 잘림·넘침을 고친다.
- Windows(PowerPoint): `$pp=New-Object -ComObject PowerPoint.Application; $p=$pp.Presentations.Open("<pptx 절대경로>",$true,$false,$false); $p.Export("<render 폴더>","PNG",1280,720); $p.Close(); $pp.Quit()`
- LibreOffice: `soffice --headless --convert-to pdf <pptx>` 뒤 PDF를 쪽마다 그림으로

### 7) 전달
`.pptx` 경로 + 구성 요약 + 폰트 의존성(다른 PC에서 해당 폰트 필요)을 보고한다.

## 출력 위치
모든 결과물은 **`<작업 폴더>/OUTPUT/ppt-design/<프로젝트명>/`** 에 모은다.
```
OUTPUT/ppt-design/<프로젝트명>/
  build.py · <파일명>.pptx · theme.json(커스텀일 때) · render/
```
- `d.save_project("<프로젝트명>","<파일>.pptx")` → 위 경로를 자동으로 만든다.
- 다른 곳에 모으려면 환경변수 `PPT_DESIGN_OUTPUT`에 폴더를 준다(그 아래 `ppt-design/<프로젝트명>/`).

## 가이드라인
- 색 절제: 주색(primary)은 강조·CTA에만. 다크 서피스로 대비/리듬.
- 텍스트 분량: 카드/셀엔 한두 문장(길면 잘림).
- 개념 정의 장은 `concept_wide`를 쓴다(긴 정의·예시도 자동 줄바꿈). `concept`는 짧은 글용.
- 한글 줄바꿈: 저장할 때 한글에 한국어 표시를 붙여 단어 단위로 줄을 바꾼다(따로 할 일 없음).
- 유형별 톤: 제안서=설득, 보고서=객관·데이터, 강의=몰입·활동, 가이드북=차분·읽힘.
- 새 레이아웃은 `layouts.py`에 추가하고 `reference/LAYOUTS.md`에 기록.
