import streamlit as st
import random

st.title("🎲 주사위 굴리기!")

if st.button("굴리기"):
    st.write("결과:", random.randint(1, 6))
