import streamlit as st

st.title("안녕하세요! Streamlit 기본 예제입니다 👋")

# 텍스트 출력
st.write("이것은 가장 간단한 Streamlit 웹앱 예제입니다!")

# 숫자 입력
number = st.number_input("숫자를 입력해보세요", min_value=0, max_value=100, value=10)

# 버튼
if st.button("버튼 클릭"):
    st.write(f"입력한 숫자는 {number} 입니다!")

