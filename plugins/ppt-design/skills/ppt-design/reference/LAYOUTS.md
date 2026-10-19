# 레이아웃 카탈로그

모든 함수는 첫 인자로 `Deck` 인스턴스(`d`)를 받고 슬라이드 1장을 추가한다.
`import layouts as L` 후 `L.함수(d, ...)` 로 호출.
**색 인자를 생략하면 코랄→틸→앰버 자동 순환.** 색은 토큰명 문자열
(`"primary"`, `"accent_teal"`, `"accent_amber"`, `"surface_dark"`, `"ink"` 등).

## 표지 · 전환 · 메시지

### `cover(d, title, subtitle="", eyebrow="", brand="", title2=None, title2_color="primary", meta="")`
표지. `title2`를 주면 2번째 줄을 강조색 ExtraBold로(1번째 줄은 Light).
- 예: `L.cover(d, title="강점으로 일하는 법", title2="잠재력 발견", subtitle="...", brand="ACME", meta="문의...")`

### `section_divider(d, number, title, subtitle="", dark=True)`
챕터 전환. 큰 번호 + 제목. `number=""`이면 번호 없이 중앙 좌측 제목만.
- 예: `L.section_divider(d, "01", "강점의 이해", "왜 중요한가")`

### `statement(d, lines, bg="surface_cream_strong")`
큰 중앙 메시지(도트 장식). 줄바꿈 `\n` 사용. 임팩트 전환용.
- 예: `L.statement(d, "인재 전쟁의 시대,\n어떻게 일하는가가\n운명을 결정한다")`

### `quote(d, quote_text, author="", bg="surface_cream_strong")`
인용/명언. 큰 따옴표 + Light 본문 + 출처.

## 학습 · 개념

### `objectives(d, title, goals, eyebrow="Learning Objectives")`
체크리스트형 학습 목표. `goals`: 문자열 리스트(권장 3~5개).

### `concept(d, term, definition, formula="", example="", eyebrow="Key Concept")`
핵심 개념: 큰 용어(Black) + 정의 + (공식 박스) + (다크 예시 콜아웃).
- 예: `L.concept(d, "강점", "재능에 지식·기술이...", formula="재능 × (지식+기술) = 강점", example="...")`

### `concept_wide(d, term, definition, formula="", example="", eyebrow="Key Concept")`
`concept` 개선판. **개념 정의 장은 이걸 먼저 쓴다.** 용어 크기를 길이에 맞춰 줄이고,
정의·예시를 공백 기준으로 다시 줄바꿈하며, 예시 상자 높이를 글 양에 맞춘다.
- 예: `L.concept_wide(d, "강점", "재능에 지식·기술이 더해져 생산적으로 발휘되는 능력", formula="재능 × (지식 + 기술) = 강점", example="‘연결’ 재능 + 커뮤니케이션 → ‘연결’ 강점")`

### `question(d, question_text, sub="")`
풀코랄 빅 퀘스천. `\n`으로 줄나눔. 청중 환기용(푸터 없음).

### `takeaways(d, title, items, eyebrow="Key Takeaways")`
핵심 N가지(최대 4). `items`: `[(소제목, 설명)]`. 넘버 + 색 라인.

## 카드 · 통계

### `three_up(d, title, cards, eyebrow="")`
3-up 피처 카드. `cards`: `[(제목, 본문)]` 또는 `[(제목, 본문, 색)]` (최대 3).

### `stat_cards(d, title, stats, eyebrow="")`
통계 카드(최대 4). `stats`: `[(숫자, 라벨, 설명)]` 또는 `[(..., 색)]`.
- 예: `L.stat_cards(d, "문제", [("13%","낮은 몰입도","설명"), ("67%","이직률","설명")])`

### `big_stat(d, number, pre="", post="", note="")`
단일 빅 통계. 거대한 숫자 1개 + 상하 설명.
- 예: `L.big_stat(d, "560%", pre="강점을 인식하면", post="더 높은 몰입도", note="* Gallup")`

## 표 · 프로세스 · 타임라인

### `comparison_table(d, title, data, highlight_col=None, eyebrow="", header_color="dark", label_col=True, intro="")`
네이티브 비교 표(편집 가능). `data`: 2차원 리스트(첫 행=헤더, 첫 열=행 라벨).
`highlight_col`: 강조할 열 인덱스(0-base). `header_color`: `"dark"` 또는 `"coral"`.
- 예: `L.comparison_table(d, "A vs B", [["","A","B"],["속도","느림","빠름"]], highlight_col=2)`

### `process(d, title, steps, eyebrow="Process")`
가로 프로세스 타임라인. `steps`: `[(제목, 설명)]` 또는 `[(..., 색)]`. 권장 3~5단계.

### `vsteps(d, title, steps, eyebrow="Process")`
세로 단계(연결선). `steps`: `[(제목, 설명)]`. 권장 3~5단계.

### `timeline(d, title, nodes, eyebrow="Timeline")`
가로 타임라인(위/아래 교차). `nodes`: `[(라벨, 제목, 보조)]`. 마지막 노드는 코랄 강조.
- 예: `L.timeline(d, "역사", [("1998","긍정심리학","셀리그만"), ("2024","새 도구","")])`

## 프레임워크 · 가이드

### `matrix_2x2(d, title, quads, note="", eyebrow="Framework", axis_label="")`
2×2 사분면. `quads`: 4개 `[(라벨, 보조)]` 순서=좌상,우상,좌하,우하.
`note`를 주면 우측에 다크 해설 패널. `axis_label`: 하단 축 라벨.

### `do_dont(d, title, dos, donts, eyebrow="Guide")`
DO/DON'T 2단. `dos`·`donts`: 문자열 리스트(각 3~4개). 초록 체크 / 빨강 X.

### `keyword_grid(d, title, words, cols=3, eyebrow="")`
키워드 그리드. `words`: `[문자열]` 또는 `[(라벨, 색)]`. `cols`로 열 수.

## 무드 · 콘텐츠

### `poster(d, headline, eyebrow="", sub="", dark=True)`
Black weight 임팩트 포스터(다크 기본). `headline`에 `\n`으로 줄나눔.

### `editorial(d, headline, columns, eyebrow="Essay")`
Thin weight 매거진/에세이. `headline`(Thin) + `columns`(본문 1~2개 리스트).

### `bullets_slide(d, title, items, eyebrow="", marker="—")`
제목 + 불릿. `items`: `[문자열]` 또는 `[(마커, 문자열)]`.

### `two_col(d, title, left, right, eyebrow="")`
2단 대비. `left`/`right`: `(헤딩, 본문, [fill], [accent])`.
본문은 문자열 또는 리스트(리스트면 불릿). fill 미지정 시 좌=크림카드, 우=다크.

### `checklist(d, title, items, dark=True, eyebrow="Summary")`
요약 체크리스트(다크 기본). `items`: 문자열 리스트.

### `worksheet(d, title, prompts, eyebrow="Activity", action="")`
활동지(빈칸). `prompts`: `[(라벨, 힌트)]`. `action`: 하단 코랄 액션 배너.

## 가이드북 · 이미지 (스크린샷 · 단계 안내)

설치/온보딩 가이드처럼 **스크린샷이 핵심**인 덱(guidebook)을 위한 레이아웃.
`image=` 에 파일 경로를 주면 비율 유지로 박스에 맞춰 들어가고, 생략하면
플레이스홀더(🖼 + 캡션)가 그려져 레이아웃이 깨지지 않는다.

### `split_image(d, title, url="", body="", chips=None, image=None, number=None, eyebrow="", title2="", title2_color="primary", caption="스크린샷")`
좌측 텍스트(번호 배지·제목·URL·본문·칩) + 우측 스크린샷. 도구/기능 소개의 표준.
`number`를 주면 좌측 큰 원형 번호. `title2`면 제목 둘째 줄을 강조색으로.
- 예: `L.split_image(d, title="Claude Desktop", title2="설치", url="https://...", body="...", chips=["macOS","Windows","무료"], number=1, image="render/claude.png")`

### `steps_image(d, title, steps, image=None, eyebrow="", caption="스크린샷")`
좌측 번호 단계(제목+설명) + 우측 스크린샷. 'How to' 안내용. `steps`: `[(제목, 설명[, 색])]` (권장 3~5).
- 예: `L.steps_image(d, "3분이면 끝", [("접속","..."),("다운로드","..."),("설치","...")], image="render/setup.png")`

### `index_list(d, title, items, eyebrow="", sub="")`
좌측 큰 타이틀 + 우측 번호 디렉터리(제목 + URL/보조). 목차·도구 목록·준비물.
`items`: `[(제목, URL/보조[, 색])]` (권장 3~6). 제목에 `\n` 사용 가능.
- 예: `L.index_list(d, "시작 전,\n준비", [("Claude 설치","https://..."), ("계정 만들기","https://...")], sub="총 6단계")`

### `feature_cards(d, title, cards, cols=None, tip="", tip_label="TIP", eyebrow="")`
N-up 카드(3~6, `three_up` 일반화). `cards`: `[(제목, 본문)]` 또는 `[(배지, 제목, 본문[, 색])]`
(배지=글자/숫자면 카드 상단 정사각 배지 + 제목 한 줄). `tip`을 주면 하단 콜아웃 밴드.
`cols` 생략 시 자동(≤5는 한 줄, 6은 3×2).
- 예: `L.feature_cards(d, "각 도구의 역할", [("C","두뇌","..."),("V","스케치북","..."), ...], tip="순서대로...")`

### `check_cards(d, title, items, eyebrow="", intro="", tip="", tip_label="TIP")`
좌측 타이틀(+안내문/TIP 밴드) + 우측 번호 체크 카드. 최종 점검·완료 확인용.
`items`: `[(제목, 설명)]` (권장 4~6). `tip_label`로 밴드 라벨 변경(예: "막히신다면").
- 예: `L.check_cards(d, "여섯 개\n모두 OK?", [("Claude 설치","앱 채팅 화면"), ...], intro="...", tip="...", tip_label="막히신다면")`

## 범용 — 제안서 · 보고서 · 강의 공통

목차·지표·가격·팀·로드맵 등 어느 덱에서나 자주 쓰는 구조들.

### `agenda(d, title, items, eyebrow="Agenda", active=None)`
목차/아젠다. 큰 번호 + 제목 행 + 구분선. `active` 인덱스만 강조. `items`: `[str]`.

### `kpi_row(d, title, kpis, eyebrow="")`
가로 KPI 행(2~5, 카드 없이 구분선). `kpis`: `[(값, 라벨[, 색])]`.
- 예: `L.kpi_row(d, "성과", [("3.2x","생산성"), ("-41%","비용"), ("98%","만족도")])`

### `pricing(d, title, plans, eyebrow="", highlight=None)`
가격 플랜(최대 3). `plans`: `[(이름, 가격, 부가, [기능들])]`. `highlight` 인덱스는 다크 카드 + "추천" 뱃지.
- 예: `L.pricing(d, "요금제", [("Basic","무료","개인",["기본"]), ("Pro","₩29,000","월",["전체","우선지원"])], highlight=1)`

### `team(d, title, people, eyebrow="")`
팀/인물 카드(최대 4, 이니셜 아바타). `people`: `[(이름, 역할[, 한줄소개])]`.

### `logos(d, title, names, cols=4, eyebrow="", note="")`
로고/도입처·파트너 그리드(텍스트 셀). `names`: `[str]`. 실제 로고는 이미지로 교체 가능.

### `roadmap(d, title, phases, eyebrow="Roadmap")`
단계/분기 로드맵 스윔레인(최대 4). `phases`: `[(라벨, 제목, [항목들])]`.
- 예: `L.roadmap(d, "로드맵", [("Q1","기반",["설계"]), ("Q2","파일럿",["적용"])])`

### `callout(d, headline, body="", eyebrow="", tone="primary", icon="!")`
단독 강조 슬라이드(풀블리드 컬러/다크). 전환·경고·핵심 한 마디. `tone`: 색 토큰 또는 `"dark"`.

### `metric_callout(d, number, title, points, pre="", eyebrow="")`
좌측 거대한 숫자 + 우측 제목·불릿 근거 패널. 임팩트 + 설명 동시. `points`: `[str]`.
- 예: `L.metric_callout(d, "560%", "몰입도 상승", ["근거 1","근거 2"], pre="강점 인식 시")`

### `feature_list(d, title, features, eyebrow="")`
2열 아이콘+제목+설명 리스트(최대 6, 카드보다 조밀).
`features`: `[(배지, 제목, 설명)]` 또는 `[(제목, 설명)]`.

### `progress_bars(d, title, bars, eyebrow="")`
가로 진행률/역량 바 리스트. `bars`: `[(라벨, 퍼센트[, 색])]`.
- 예: `L.progress_bars(d, "역량", [("발상", 82), ("평가", 91)])`

### `swot(d, title, quads, eyebrow="SWOT")`
4분면(색 헤더 + 불릿). `quads`: 4개 `[(헤더, [항목들])]` 순서=좌상,우상,좌하,우하(틸/코랄/앰버/레드).

### `compare_cards(d, title, left, right, eyebrow="", verdict="")`
좌우 큰 대비 카드 + 중앙 VS 배지. before/after·경쟁 비교. `left·right`: `(헤딩, [항목들][, 강조색])`.

### `image_full(d, title="", caption="", image=None, eyebrow="")`
풀블리드 이미지 + 하단 다크 캡션 밴드. `image` 없으면 다크 플레이스홀더.

### `image_grid(d, title, items, eyebrow="", cols=None)`
이미지 갤러리 그리드 + 캡션. `items`: `[(이미지경로, 캡션)]` (경로 None이면 플레이스홀더).

## 차트

### `chart(d, title, categories, series, kind="column", eyebrow="", note="")`
네이티브 차트(편집 가능). `categories`: 문자열 리스트.
`series`: `[(이름, [값들])]`. `kind`: `"column"` | `"line"` | `"donut"`.
시리즈 색은 코랄/틸/앰버/다크 자동 적용.
- 예: `L.chart(d, "분포", ["발상","탐색","평가"], [("팀", (6,4,5))], kind="column")`
- 도넛: `L.chart(d, "비중", ["A","B","C"], [("점유율", (40,35,25))], kind="donut")`

## 마무리

### `closing(d, title, sub="", contact="", eyebrow="", action="")`
어두운 배경 가운데 정렬 마무리. `contact`만 주면 버튼에 연락처를, `action`(예: "문의하기")을 주면 버튼엔 action, 그 아래 contact를 작게 쓴다. `eyebrow`는 제목 위 작은 글.

### `closing_qr(d, title, sub="", offers=None, qr=None, contacts=None, eyebrow="GET STARTED", qr_caption="", qr_url="", deco=None, offer_label="", dark=True)`
마무리 3열: 왼쪽 오퍼 카드(`offers=[(제목, 설명)]`) + 가운데 QR 그림(`qr`=이미지 경로) + 아래 연락처(`contacts=[(라벨, 값)]`, 최대 3).
`deco`에 검정 배경 렌더 이미지를 주면 검정을 배경색으로 바꿔 오른쪽에 얹는다.
- 예: `L.closing_qr(d, "지금 시작해 보세요", sub="설치는 두 줄", offers=[("무료 설치","GitHub")], qr="render/qr.png", qr_caption="GitHub", contacts=[("메일","hello@acme.com")])`

### `big_message(d, lines, eyebrow="", sub="", note="", dark=True, size=None)`
큰 문장 2~3줄 임팩트 장. `poster`보다 긴 문장에 맞는다. `lines`는 줄마다 `[(문자열, 색|None), ...]` — 한 줄 안에서 일부만 강조색.
- 예: `L.big_message(d, [[("말로 하면", None)], [("설명을 ", None), ("안 줄여요", "primary")]], sub="...")`

## 사진 · 실화면 (사진·스크린샷이 있을 때)

`image`·`photos`·`shots`에 파일 경로를 준다. 없거나 경로가 틀리면 자리 표시(🖼)가 대신 들어가 레이아웃이 깨지지 않는다.
사진은 박스를 꽉 채우게 잘리고(`anchor`로 살릴 쪽 지정: center|left|right|top|bottom), 스크린샷은 자르지 않고 카드 안에 온전히 들어간다(흰 여백은 먼저 잘라 냄).
잘라 낸 그림은 임시 폴더(`ppt-design-imgcache`)에 둔다. 작업 폴더를 어지럽히지 않는다.

### `cover_photo(d, title_lines, eyebrow="", brand="", sub="", meta="", photos=None, accent_from=1, pill=True, dark=False)`
표지: 왼쪽 큰 헤드라인(줄 리스트) + 오른쪽 아래 사진 조각 최대 3장(알약 모양). `accent_from` 번째 줄부터 강조색.
- 예: `L.cover_photo(d, ["말하면 정리돼서", "입력창에 들어가요"], eyebrow="GUIDE", brand="ACME", sub="...", photos=["a.jpg","b.jpg","c.jpg"])`

### `photo_hero(d, title_lines, body="", note="", image=None, anchor="right", ratio=0.5, dark=False, brand="", eyebrow="")`
한쪽(기본 오른쪽 절반)이 사진, 반대쪽에 헤드라인·본문·강조 한 줄(`note`).

### `split_color_photo(d, title_lines, body="", items=None, footer_note="", image=None, eyebrow="", color="primary", ratio=0.5, anchor="center")`
왼쪽 색 블록(제목·본문·항목 `items=[(라벨, 설명)]`) + 오른쪽 사진. 워크숍·프로그램 소개용.

### `stats_photo(d, title, stats, image=None, eyebrow="", note="", anchor="center")`
왼쪽 수치 카드 3장 세로(`stats=[(숫자, 라벨, 설명, 출처)]`) + 오른쪽 사진 + 아래 한 줄 해설.

### `shots_row(d, title, shots, eyebrow="", sub="", desc="", note="", note_label="", note_sub="", bg=None)`
스크린샷 3장 가로 + 번호 캡션(`shots=[(경로, 캡션)]`). 아래 `note` 밴드와 오른쪽 `note_label`(TIP 등).

### `screens_showcase(d, title, shots, eyebrow="", desc="", note="", note2="", bg="surface_soft", on_dark=False)`
제품 실화면 2장(큰 화면 + 작은 화면). `shots=[(경로, 캡션)]`.

### `profile_photo(d, name, name_en="", role="", career=None, activity=None, image=None, eyebrow="", title="대표 강사 프로필", note="")`
인물 프로필: 왼쪽 사진 + 오른쪽 2열 이력(`career`·`activity` 문자열 리스트) + 강조 한 줄.

### `logo_sheet(d, title, image=None, eyebrow="", sub="", names=None, cols=6)`
도입처 로고: 로고 모음 그림(`image`)을 크게. 그림이 없으면 `names`를 글자 칸으로 늘어놓는다.

## 정리 · 후기 · 지도

### `quote_grid(d, title, quotes, eyebrow="", desc="")`
후기 2×2. `quotes=[(본문, 화자)]` 최대 4.

### `radial_map(d, title, center, center_sub="", groups=None, desc="", eyebrow="", radius=178, node=96, cx=420, cy=430, foot_note="")`
방사형 개념 지도: 가운데 원 + 둘레 노드 + 오른쪽 묶음 카드. `groups=[(묶음 이름, 영문, 색 토큰, [(노드, 영문), ...])]`.
- 예: `L.radial_map(d, "생각의 지도", "AI", groups=[("만들기","Make","primary",[("글",""),("그림","")]), ("찾기","Find","accent_teal",[("검색","")])])`

---

## 새 레이아웃 추가 방법
1. `deck/layouts.py`에 `def 새이름(deck, ...):` 함수 추가
   (`deck.add(bg)`로 슬라이드 생성, `helpers`의 `rect/oval/text/...` 사용,
   끝에 `deck.footer(s)` 호출).
2. 이 문서에 시그니처·설명 추가.
3. 좌표계는 1280×720 px. `LX=80`, 콘텐츠 폭 `CW=1120`.
