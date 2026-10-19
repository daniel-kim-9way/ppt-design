# PPT Design

**디자인 시스템으로 PPT를 만드는 Claude Code 스킬.**
글꼴과 색(테마)을 정하면, 같은 내용이 그 스타일의 고칠 수 있는 `.pptx`로 나와요.
제안서 · 보고서 · 강의 · 가이드북 같은 **덱 유형**마다 구성을 다르게 짜 줘요.

> 한국어 슬라이드에 맞춰 뒀어요. 한글은 단어 단위로 줄을 바꾸고, 영문 글꼴 테마에서도 한글은 Pretendard로 그려요.
> 표와 차트는 파워포인트에서 바로 고칠 수 있는 진짜 표·차트로 들어가요.

---

## 설치

### 1) Claude Code에서 한 줄 (Claude Code 2.1.275 이상)

```
/plugin install ppt-design --marketplace daniel-kim-9way/ppt-design
```

버전이 낮으면 두 줄로 해요.

```
/plugin marketplace add daniel-kim-9way/ppt-design
/plugin install ppt-design@ppt-design
```

설치가 끝나면 Claude Code를 다시 열거나 `/reload-plugins`를 치세요. 버전은 터미널에서 `claude --version`으로 봐요.

### 2) 파이썬 라이브러리 한 번

```
pip install python-pptx
```

Windows에서 `pip`이 없다고 나오면 `py -m pip install python-pptx`를 치세요. 처음 덱을 만들 때 Claude에게 «설치해 줘»라고 해도 돼요.

### 3) 글꼴 (권장)

기본 테마는 [Pretendard](https://github.com/orioncactus/pretendard)를 써요. 없어도 만들어지지만, 다른 글꼴로 대신 보여요.

<details>
<summary>플러그인 없이 개인 스킬로 넣기</summary>

```
git clone https://github.com/daniel-kim-9way/ppt-design
```
받은 폴더의 `plugins/ppt-design/skills/ppt-design`를 `~/.claude/skills/ppt-design`로 복사해요.
</details>

---

## 첫 덱 만들기

Claude Code에 그냥 말하세요.

```
회의 잘하는 법을 주제로 4장짜리 강의안 PPT 만들어 줘
```

Claude가 유형·테마 확인 → 슬라이드 기획 → 빌드 → 그림으로 뽑아 확인 → 전달까지 해요.
결과물은 **작업 폴더의 `OUTPUT/ppt-design/<프로젝트>/`**에 생겨요(`build.py`도 같이 있어서 고쳐 다시 만들 수 있어요).

### 내 스타일로 만들기: DESIGN.md

잘 알려진 사이트의 디자인(색·글꼴·여백)을 정리한 `DESIGN.md`를 덱 스타일로 쓸 수 있어요.

- 무료 모음: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — `design-md/<사이트>/DESIGN.md`를 받아요.
- 더 많은 목록: [getdesign.md](https://getdesign.md/design-md) — 일부는 유료(Catalog Pass)이거나 로그인이 필요해요.

받은 `DESIGN.md`를 작업 폴더에 두고 이렇게 말해요.

```
DESIGN.md를 이 프로젝트의 덱 스타일로 써 줘. 이 내용으로 제안서 만들어 줘: ...
```

### 스타일을 정하는 다른 방법

| 이렇게 말하면 | 결과 |
|---|---|
| (그냥 만들어 줘) | 기본 **cream-coral** 테마 |
| "**slate-blue** 테마로" | 프리셋 그대로 (`cream-coral` · `slate-blue` · `ink-mono` · `voltagent-dark`) |
| "주색 **#2563EB**, 글꼴 **Pretendard**로" | 색·글꼴 몇 개로 전체 팔레트 자동 생성 |
| "`DESIGN.md` 스타일로" | 명세의 색·글꼴로 테마 변환 |

### 고치기

"3번 슬라이드 문구 바꿔 줘", "다크로 바꿔 줘", "차트 하나 넣어 줘"라고 하면
`OUTPUT/ppt-design/<프로젝트>/build.py`를 고쳐 다시 만들어요.

---

## 들어 있는 것

- 🎨 **테마 교체**: 프리셋 4개 또는 글꼴+색 몇 개로 팔레트 자동 생성(`theme.from_seeds`). 라이트·다크 둘 다.
- 📥 **DESIGN.md → 테마**: 명세의 색·글꼴로 테마를 만들어요(`reference/DESIGN-MD.md`).
- 🧩 **레이아웃 58종**: 표지 · 통계 · 카드 · 비교표 · 프로세스 · 타임라인 · 매트릭스 · Do/Don't · 인용 · 활동지 · 포스터 · 차트 · 마무리 · 목차 · KPI · 가격표 · 팀 · 로드맵 · SWOT · 스크린샷 안내 ·
  **사진 레이아웃**(사진 표지 · 사진 반쪽 · 사진+수치 · 스크린샷 3장/2장 · 인물 프로필 · 로고 모음) · 후기 2×2 · 방사형 지도 · QR 마무리 · 큰 문장. 목록은 `reference/LAYOUTS.md`.
- 📑 **덱 유형 4가지**: proposal · report · lecture · guidebook — 유형마다 추천 흐름.
- ✏️ **고칠 수 있는 결과물**: 글·표·차트가 전부 파워포인트 개체.
- 🇰🇷 **한글**: 단어 단위 줄바꿈, 영문 글꼴 테마에서도 한글은 Pretendard.

## 코드로 바로 쓰기

```python
import sys
sys.path.insert(0, "plugins/ppt-design/skills/ppt-design/deck")   # 저장소에서 실행할 때
from builder import Deck
import layouts as L

d = Deck(theme="slate-blue", kind="proposal", brand="ACME")
L.cover(d, title="제안서", title2="핵심 가치", subtitle="부제", brand="ACME")
L.stat_cards(d, "왜 지금인가", [("3x", "속도", "...")])
L.process(d, "도입 절차", [("진단", "..."), ("설계", "..."), ("적용", "...")])
L.closing(d, "함께 시작하시죠", contact="hello@acme.com")
print(d.save_project("acme-proposal", "ACME.pptx"))
# → ./OUTPUT/ppt-design/acme-proposal/ACME.pptx
```

예제: `python examples/example_lecture.py` (저장소 루트에서). 결과물 위치를 바꾸려면 환경변수 `PPT_DESIGN_OUTPUT`에 폴더를 줘요.

### 내 테마

```python
import theme as th
t = th.from_seeds(font="Pretendard", primary="#2563EB", canvas="#FFFFFF",
                  ink="#0F172A", dark="#0B1220", name="acme")
th.save(t, "OUTPUT/ppt-design/acme/theme.json")
# Deck(theme="OUTPUT/ppt-design/acme/theme.json", ...)
```
글꼴이 Inter처럼 한글이 없는 영문 글꼴이면 `ko="Pretendard"`를 같이 줘요. 자세한 건 `reference/THEMES.md`.

## 문서

- `plugins/ppt-design/skills/ppt-design/SKILL.md` — Claude가 따르는 작업 순서
- `.../reference/LAYOUTS.md` — 레이아웃 58종
- `.../reference/THEMES.md` — 테마 구조·만들기
- `.../reference/DESIGN-MD.md` — DESIGN.md를 테마로 바꾸는 법
- `.../reference/DECK-TYPES.md` — 유형별 구성

## 한계

- python-pptx는 글꼴을 파일에 넣지 못해요. 보는 PC에도 같은 글꼴이 있어야 똑같이 보여요.
- 16:9(1280×720) 전용이에요.
- 그림으로 뽑아 확인하려면 PowerPoint(Windows) 또는 LibreOffice가 있어야 해요. 만드는 데는 필요 없어요.

## License

MIT — `LICENSE`를 보세요.
