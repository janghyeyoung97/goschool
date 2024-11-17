import streamlit as st
import pandas as pd

# 세션 상태 초기화
if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

# 사이드바에 사용자 ID 표시
with st.sidebar:
    st.caption(f'{ID}님 접속중')

# CSV 파일 불러오기
data = pd.read_csv("대학위치.csv")

# 제목 설정
st.title('전국 대학 위치 지도')

st.subheader("너의 생각보다 대학은 훨씬 많단다")


# 데이터 전처리
data = data.copy().fillna(0)
data.loc[:, 'size'] = 5  # 마커 크기 설정

# 마커 색상 설정 (학교구분에 따라)
color = {
    '대학교': '#3498db',   # 파란색
    '전문대학': '#e74c3c', # 빨간색
    '사이버대학': '#2ecc71' # 초록색
}
data.loc[:, 'color'] = data['학교구분'].map(color).fillna('#95a5a6')  # 기본 색상 회색

# 지도에 데이터 표시
st.map(data, latitude="위도", longitude="경도", size="size", color="color")

# 데이터 프레임 표시
st.subheader("대학 위치 데이터")
st.dataframe(data)
