# 덱 유형 (kind)

`Deck(kind="...")`로 지정. 유형은 **추천 구성(흐름)과 톤**을 안내한다.
`python deck/decktypes.py <kind>` 로 흐름을 출력해볼 수 있다.

## proposal — 제안서
**톤**: 설득·신뢰. 문제→솔루션→근거→실행→가격→CTA. 주색은 핵심 주장·CTA에만.
**흐름**: cover → statement(문제) → stat_cards(규모) → three_up(솔루션) →
comparison_table(우위) → process(실행) → timeline(일정) → two_col(효과vs비용) →
big_stat(ROI) → quote(레퍼런스) → closing(CTA)

## report — 보고서
**톤**: 객관·간결. 요약 먼저(Executive Summary), 데이터·표·차트 중심. 색 절제.
**흐름**: cover → bullets_slide(요약) → section_divider(현황) → stat_cards(지표) →
chart(추세) → comparison_table(비교) → section_divider(분석) → two_col(잘된점/개선점)
→ matrix_2x2(우선순위) → section_divider(결론) → takeaways(결론) → checklist(액션) →
closing

## lecture — 강의
**톤**: 이해·몰입. 학습목표→개념→사례→활동→요약. 무드 다양(poster/editorial).
**흐름**: cover → statement(핵심) → objectives(목표) → section_divider → concept(개념)
→ question(환기) → stat_cards(사례) → three_up(핵심3) → do_dont(권장/주의) →
process(단계) → worksheet(활동) → poster(임팩트) → checklist(요약) → closing

## guidebook — 가이드북
**톤**: 차분·읽힘. 한 슬라이드 한 주제, 단계·체크리스트·예시 풍부. 에디토리얼 톤.
**흐름**: cover → bullets_slide(개요) → section_divider(Part1) → concept(정의) →
vsteps(절차) → editorial(원리, 긴 글) → do_dont(베스트프랙티스) → worksheet(템플릿) →
comparison_table(옵션) → checklist(완료) → quote(팁) → closing

---
이 흐름은 **출발점**이다. 내용에 맞게 레이아웃을 더하거나 빼고, 같은 레이아웃이
3장 이상 연속되지 않게 섞는다. 전체 카탈로그는 `LAYOUTS.md` 참고.
