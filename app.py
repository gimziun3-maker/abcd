import streamlit as st
from streamlit_sortables import sort_items
import random

st.title("🧲 드래그로 팀 나누기")

st.write("이름들을 입력한 뒤 팀 수를 정하면 드래그해서 팀을 재배치할 수 있어요!")

names_text = st.text_area("이름 목록", "철수\n영희\n민수\n지영\n가영")
team_count = st.number_input("팀 수", min_value=1, value=2, step=1)

if st.button("팀 만들기"):
    names = [n.strip() for n in names_text.split("\n") if n.strip()]
    random.shuffle(names)

    teams = [[] for _ in range(team_count)]
    for i, name in enumerate(names):
        teams[i % team_count].append(name)

    st.session_state["teams"] = teams

if "teams" in st.session_state:
    st.subheader("🔧 드래그해서 팀 조정하기")

    new_teams = sort_items(
        st.session_state["teams"],
        multi_containers=True,
        direction="horizontal",
        key="sortable"
    )

    st.session_state["teams"] = new_teams

    for i, t in enumerate(new_teams, 1):
        st.write(f"### 팀 {i}")
        st.write(", ".join(t) if t else "⚠️ 팀이 비었어요")
