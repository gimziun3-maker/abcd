import streamlit as st
import random

st.title("🎲 랜덤 팀 뽑기 앱")

st.write("이름을 줄바꿈(엔터)으로 넣어주세요!")

names_text = st.text_area("이름 목록", "철수\n영희\n민수\n지영")
team_count = st.number_input("팀 수", min_value=1, value=2, step=1)

if st.button("팀 나누기"):
    names = [n.strip() for n in names_text.split("\n") if n.strip()]

    if len(names) < team_count:
        st.error("팀 수보다 이름이 더 많아야 해요!")
    else:
        random.shuffle(names)
        teams = [[] for _ in range(team_count)]

        # 이름을 팀에 라운드로빈 방식 배정
        for i, name in enumerate(names):
            teams[i % team_count].append(name)

        # 출력
        for idx, team in enumerate(teams, 1):
            st.subheader(f"팀 {idx}")
            st.write(", ".join(team))
