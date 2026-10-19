# -*- coding: utf-8 -*-
"""
덱 유형(kind)별 추천 구성. 빌드 스크립트를 짤 때 이 흐름을 참고해 레이아웃을
배치한다. (코드를 자동 생성하지 않는다 — 기획 가이드)
flow: (레이아웃 함수, 목적) 리스트.
"""
TYPES = {
    "proposal": {
        "title": "제안서 (Proposal)",
        "tone": "설득·신뢰. 문제→솔루션→근거→실행→가격→CTA. 코랄은 핵심 주장·CTA에만.",
        "flow": [
            ("cover", "제안 제목 + 한 줄 가치"),
            ("statement", "고객의 핵심 문제를 한 문장으로"),
            ("stat_cards", "문제의 규모·근거 수치"),
            ("three_up", "우리 솔루션 3가지 축"),
            ("comparison_table", "경쟁/기존 방식 대비 우위"),
            ("process", "도입/실행 단계"),
            ("timeline", "일정·마일스톤"),
            ("two_col", "기대 효과 vs 비용"),
            ("big_stat", "핵심 ROI 한 방"),
            ("quote", "레퍼런스/고객 보증"),
            ("closing", "다음 단계 · 연락처(CTA)"),
        ],
    },
    "report": {
        "title": "보고서 (Report)",
        "tone": "객관·간결. 요약 먼저(Executive Summary), 데이터·표·차트 중심. 색 절제.",
        "flow": [
            ("cover", "보고 제목 + 기간/작성자"),
            ("bullets_slide", "핵심 요약 (Executive Summary)"),
            ("section_divider", "1. 현황"),
            ("stat_cards", "핵심 지표 현황"),
            ("chart", "추세/분포 (네이티브 차트)"),
            ("comparison_table", "기간/항목 비교 표"),
            ("section_divider", "2. 분석"),
            ("two_col", "잘된 점 / 개선점"),
            ("matrix_2x2", "우선순위·리스크 프레임"),
            ("section_divider", "3. 결론·제언"),
            ("takeaways", "핵심 결론 3가지"),
            ("checklist", "액션 아이템"),
            ("closing", "마무리·문의"),
        ],
    },
    "lecture": {
        "title": "강의 (Lecture)",
        "tone": "이해·몰입. 학습목표→개념→사례→활동→요약. 무드 다양(포스터/에디토리얼).",
        "flow": [
            ("cover", "강의 제목"),
            ("statement", "한 줄 핵심 메시지"),
            ("objectives", "학습 목표"),
            ("section_divider", "섹션 전환"),
            ("concept", "핵심 개념(+공식/예시)"),
            ("question", "청중 환기 질문"),
            ("stat_cards", "근거 수치 / 사례"),
            ("three_up", "핵심 3가지"),
            ("do_dont", "권장/주의"),
            ("process", "단계 흐름"),
            ("worksheet", "직접 해보는 활동"),
            ("poster", "임팩트 한 마디"),
            ("checklist", "요약"),
            ("closing", "마무리"),
        ],
    },
    "guidebook": {
        "title": "가이드북 (Guidebook)",
        "tone": "차분·읽힘. 한 슬라이드 한 주제, 단계·체크리스트·예시 풍부. 에디토리얼 톤.",
        "flow": [
            ("cover", "가이드 제목 + 부제"),
            ("bullets_slide", "이 가이드로 할 수 있는 것"),
            ("section_divider", "Part 1"),
            ("concept", "개념 정의"),
            ("vsteps", "절차 단계별"),
            ("editorial", "배경/원리 설명(긴 글)"),
            ("do_dont", "베스트 프랙티스"),
            ("worksheet", "따라하기 템플릿"),
            ("comparison_table", "옵션 비교"),
            ("checklist", "완료 체크리스트"),
            ("quote", "팁/명언"),
            ("closing", "다음 가이드 안내"),
        ],
    },
}


def flow(kind):
    """유형의 추천 흐름을 텍스트로 반환."""
    t = TYPES.get(kind)
    if not t:
        return f"unknown kind: {kind}. choices: {list(TYPES)}"
    lines = [f"[{t['title']}] {t['tone']}", ""]
    for i, (lo, why) in enumerate(t["flow"], 1):
        lines.append(f"{i:2d}. L.{lo:<18} — {why}")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    print(flow(sys.argv[1] if len(sys.argv) > 1 else "lecture"))
