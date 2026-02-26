import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 선호도 통계")

# 샘플 데이터
data = pd.DataFrame({
    '메뉴': ['슈팅스타', '아몬드봉봉', '엄마는외계인'],
    '득표수': [10, 25, 15]
})

fig = px.bar(data, x='메뉴', y='득표수', color='메뉴', title="인기 메뉴 순위")
st.plotly_chart(fig)
