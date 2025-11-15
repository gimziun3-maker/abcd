import streamlit as st

st.title("사이드바 예제 🧭")

lang = st.sidebar.selectbox("언어를 선택하세요", ["Python", "JavaScript", "C++"])
st.write(f"선택한 언어: **{lang}**")



