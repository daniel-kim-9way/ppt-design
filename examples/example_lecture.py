# -*- coding: utf-8 -*-
"""예제: 기본 테마(cream-coral)로 짧은 강의 덱. 현재 폴더의 OUTPUT/ppt-design/에 생성.

실행: python examples/example_lecture.py   (저장소 루트에서)
"""
import os
import sys
here = os.path.dirname(os.path.abspath(__file__))
candidates = [
    os.path.join(here, "..", "plugins", "ppt-design", "skills", "ppt-design", "deck"),   # 저장소에서 실행
    os.path.join(os.path.expanduser("~"), ".claude", "skills", "ppt-design", "deck"),     # 개인 스킬로 복사한 경우
]
sys.path.insert(0, next(os.path.abspath(p) for p in candidates if os.path.isdir(p)))
from builder import Deck
import layouts as L

d = Deck(theme="cream-coral", kind="lecture", brand="Example · PPT Design")

L.cover(d, title="강점으로 일하는 법", title2="나와 팀의 잠재력",
        subtitle="뇌과학 기반 강점 워크숍", brand="DECK", eyebrow="LECTURE")
L.objectives(d, "이 강의가 끝나면", [
    "강점이 무엇인지 정의할 수 있다",
    "나의 대표 강점을 설명할 수 있다",
    "팀에서 강점을 활용하는 법을 안다",
])
L.concept_wide(d, "강점", "재능에 지식·기술이 더해져 생산적으로 발휘되는 능력",
               formula="재능 × (지식 + 기술) = 강점",
               example="‘연결’ 재능 + 커뮤니케이션 → ‘연결’ 강점")
L.stat_cards(d, "강점을 모르면", [
    ("13%", "낮은 몰입도", "세계 평균보다 낮음"),
    ("67%", "높은 이직률", "강점 미활용 시"),
])
L.process(d, "강점 개발 4단계", [
    ("발견", "진단"), ("이해", "맥락"), ("적용", "활용"), ("성장", "축적")])
L.do_dont(d, "강점 코칭",
          dos=["강점에 맞는 역할", "구체적 피드백"],
          donts=["약점만 지적", "같은 잣대"])
L.poster(d, "강점에\n집중하라", eyebrow="MINDSET", sub="약점 보완보다 강점 확장")
L.closing(d, "함께 시작하시죠", sub="PPT Design", contact="hello@example.com")

print(d.save_project("example-lecture", "Example_Lecture.pptx"))
