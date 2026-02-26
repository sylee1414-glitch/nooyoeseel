import streamlit as st

# 페이지 설정 (웹 브라우저 탭에 표시될 이름)
st.set_page_config(page_title="나의 첫 웹 앱", page_icon="🏠")

st.title('🏠 나의 첫 웹 서비스 만들기!')
st.write("반갑습니다! 왼쪽 사이드바를 이용해 페이지를 이동해보세요.")

name = st.text_input('이름을 입력해주세요: ')
menu = st.selectbox('좋아하는 음식을 선택해주세요: ', ['슈팅스타', '아몬드봉봉', '엄마는외계인'])

if st.button('인사말 생성'):
    st.success(f"{name}님! 당신이 좋아하는 음식은 {menu}이군요?! 저도 좋아요!!")
