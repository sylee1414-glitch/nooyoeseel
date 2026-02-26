import streamlit as st

st.set_page_config(page_title="나의 첫 웹 앱", page_icon="🏠", layout="wide")

st.title('🏠 나의 첫 웹 서비스!')
st.write("원하시는 메뉴를 선택하세요.")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("📊 일반 통계 분석")
        st.write("업로드된 CSV 파일을 바탕으로 기본적인 데이터 현황을 파악합니다.")
        if st.button("통계 페이지로 이동", use_container_width=True):
            st.switch_page("pages/01_첫페이지.py")

with col2:
    with st.container(border=True):
        st.subheader("🧬 세계의 MBTI 분석")
        st.write("전 세계 사람들의 MBTI 분포를 인터랙티브 그래프로 확인합니다.")
        # 파일명이 정확해야 합니다 (예: 02_🧬_MBTI.py)
        if st.button("MBTI 분석 보기", use_container_width=True):
            st.switch_page("pages/02_두번째페이지.py")

with col3:
    with st.container(border=True):
        st.subheader("🧬 세계 MBTI")
        st.write("countries.csv 데이터를 읽어 국가별 통계를 분석합니다.")
        # 파일명이 02_🧬_MBTI.py 라고 가정
        if st.button("MBTI 페이지로 이동", use_container_width=True):
            st.switch_page("pages/03_세번째페이지.py")
            

st.markdown("---")
# 하단에 간단한 인사말 섹션
st.info("💡 오른쪽 사이드바 메뉴를 통해서도 언제든지 페이지 이동이 가능합니다.")
