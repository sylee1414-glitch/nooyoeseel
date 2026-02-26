import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("📂 업로드된 데이터 분석")

# 1. 파일 경로 설정 (최상위 폴더의 data.csv)
# pages 폴더 안에서 실행되더라도 상위 폴더의 파일에 접근 가능합니다.
file_path = 'data.csv'

# 2. 파일 존재 여부 확인 후 읽기
if os.path.exists(file_path):
    # 한글 깨짐 방지를 위해 encoding 설정 (필요시 cp949로 변경)
    try:
        df = pd.read_csv(file_path, encoding='utf-8')
    except:
        df = pd.read_csv(file_path, encoding='cp949')

    st.success("✅ 데이터를 성공적으로 불러왔습니다!")

    # 3. 데이터 보여주기
    st.subheader("데이터 미리보기")
    st.dataframe(df, use_container_width=True)

    # 4. 데이터 기반 그래프 (예: 첫 번째 열이 이름, 두 번째 열이 수치라고 가정)
    st.subheader("📊 데이터 시각화")
    
    # 열 이름 선택 (사용자가 직접 선택하게 할 수도 있습니다)
    cols = df.columns.tolist()
    x_axis = st.selectbox("X축 선택", cols, index=0)
    y_axis = st.selectbox("Y축 선택", cols, index=1 if len(cols) > 1 else 0)

    fig = px.bar(df, x=x_axis, y=y_axis, color=x_axis, title=f"{x_axis}별 {y_axis} 현황")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("⚠️ 최상위 폴더에 'data.csv' 파일이 없습니다.")
    st.info("파일을 업로드하거나 이름을 확인해 주세요.")
