import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🔥 실시간 칼로리 트래커")

# 데이터 저장을 위한 세션 초기화
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['음식', '칼로리'])

# 입력 양식
with st.form("input_form"):
    food = st.text_input("음식 이름")
    cal = st.number_input("칼로리(kcal)", min_value=0)
    submitted = st.form_submit_button("추가하기")

if submitted and food:
    new_row = pd.DataFrame({'음식': [food], '칼로리': [cal]})
    st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)

# 그래프 표시
if not st.session_state.df.empty:
    fig = px.pie(st.session_state.df, values='칼로리', names='음식', hole=0.3)
    st.plotly_chart(fig)
    st.metric("오늘 총 섭취량", f"{st.session_state.df['칼로리'].sum()} kcal")
