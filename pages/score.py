import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# CSV 파일 불러오기
file_path = "2024수능.csv"
data = pd.read_csv(file_path)

# 데이터 타입 변환 (쉼표 제거 후 숫자로 변환)
data["표준점수"] = pd.to_numeric(data["표준점수"].apply(lambda x: str(x).replace(',', '')), errors="coerce")
data["남자인원"] = pd.to_numeric(data["남자인원"].apply(lambda x: str(x).replace(',', '')), errors="coerce")
data["여자인원"] = pd.to_numeric(data["여자인원"].apply(lambda x: str(x).replace(',', '')), errors="coerce")
data["전체인원"] = pd.to_numeric(data["전체인원"].apply(lambda x: str(x).replace(',', '')), errors="coerce")

# 세션 상태 초기화
if "ID" not in st.session_state:
    st.session_state["ID"] = "None"

ID = st.session_state["ID"]

# 사이드바에 사용자 ID 표시
with st.sidebar:
    st.caption(f'{ID}님 접속중')

# 제목 설정
st.title("2024 수능 표준점수 분석")

st.subheader("2024학년도 수능 국어, 수학 표준점수 분포 알아보기")

# 드롭다운으로 과목과 인원 선택
subject = st.selectbox("과목 선택", data['과목'].unique())
person_type = st.multiselect("인원 선택", ["남자인원", "여자인원", "전체인원"])

# 선택된 과목에 맞게 데이터 필터링
filtered_data = data[data['과목'] == subject]

# 표준점수 기준으로 정렬
filtered_data = filtered_data.sort_values(by="표준점수")

# 그래프 그리기
st.subheader(f"{subject} 과목의 표준점수별 인원 비교 그래프")

# 그래프 데이터 준비
plt.figure(figsize=(10, 6))

# 선택된 인원 유형에 따라 그래프 그리기
for person in person_type:
    plt.plot(filtered_data["표준점수"], filtered_data[person], marker='o', linestyle='-', label=person)

# 그래프 설정
plt.xlabel("표준점수")
plt.ylabel("인원 수")
plt.title(f"{subject} 과목의 표준점수별 인원 비교 그래프")
plt.legend()
plt.grid()

# Streamlit에 그래프 표시
st.pyplot(plt)

# 데이터 프레임 표시
st.subheader("필터링된 데이터")
st.dataframe(filtered_data)
