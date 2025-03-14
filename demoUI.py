import pandas as pd
import streamlit as st



st.title("Ứng dụng Streamlit đầu tiên của tôi")
st.write("Xin chào! Đây là ứng dụng Streamlit đầu tiên của tôi.")

name = st.text_input("Tên của bạn là gì?")
if name:
    st.write(f"Xin chào, {name}!")
    
    # Tạo DataFrame mẫu
df = pd.DataFrame({
    'Tên': ['An', 'Bình', 'Cường'],
    'Tuổi': [25, 30, 22],
    'Thành phố': ['Hà Nội', 'TP.HCM', 'Đà Nẵng']
})

# Hiển thị dữ liệu
st.write("### Dữ liệu người dùng")
st.write(df)  # Hiển thị toàn bộ DataFrame
st.write(df.head())  # Hiển thị 5 dòng đầu tiên
st.table(df)  # Hiển thị dưới dạng bảng tĩnh
st.dataframe(df)  # Hiển thị dưới dạng bảng tương tác

if st.button("Nhấn vào tôi"):
    st.write("Bạn đã nhấn nút!")

# Hộp chọn
option = st.selectbox("Chọn một thành phố:", ["Hà Nội", "TP.HCM", "Đà Nẵng"])
st.write(f"Bạn đã chọn: {option}")

# Thanh trượt
age = st.slider("Chọn tuổi:", 0, 100, 25)
st.write(f"Tuổi đã chọn: {age}")

# Nhập văn bản
user_input = st.text_input("Nhập nội dung:")
if user_input:
    st.write(f"Bạn đã nhập: {user_input}")

# Tải file lên
uploaded_file = st.file_uploader("Chọn một file CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dữ liệu từ file:")
#    st.write(df)
    st.write(df.head())