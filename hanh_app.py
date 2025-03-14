import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Thiết lập tiêu đề
st.title("Data Analytics")

# Tải lên file CSV hoặc Excel
uploaded_file = st.file_uploader("Tải lên file CSV hoặc Excel", type=["csv", "xlsx"])

if uploaded_file:
    # Đọc file vào DataFrame
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Hiển thị dữ liệu
    st.write("### Dữ liệu đã tải lên:")
    st.dataframe(df)

    # Lựa chọn loại biểu đồ
    chart_type = st.selectbox("Chọn loại biểu đồ", ["Line Chart", "Bar Chart", "Pie Chart"])

    # Xử lý Line Chart và Bar Chart
    if chart_type in ["Line Chart", "Bar Chart"]:
        numerical_columns = df.select_dtypes(include=['number']).columns
        if len(numerical_columns) >= 2:
            x_col = st.selectbox("Chọn cột trục X", numerical_columns)
            y_col = st.selectbox("Chọn cột trục Y", numerical_columns)

            st.write(f"### {chart_type}")
            if chart_type == "Line Chart":
                st.line_chart(df.set_index(x_col)[y_col])
            else:
                st.bar_chart(df.set_index(x_col)[y_col])
        else:
            st.warning("Dữ liệu không có đủ cột số để vẽ biểu đồ.")

    # Xử lý Pie Chart
    elif chart_type == "Pie Chart":
        category_columns = df.select_dtypes(include=['object']).columns
        numerical_columns = df.select_dtypes(include=['number']).columns

        if len(category_columns) > 0 and len(numerical_columns) > 0:
            category_col = st.selectbox("Chọn cột danh mục (category)", category_columns)
            value_col = st.selectbox("Chọn cột giá trị (numerical)", numerical_columns)

            # Tổng hợp dữ liệu theo danh mục
            pie_data = df.groupby(category_col)[value_col].sum()

            # Vẽ Pie Chart bằng Matplotlib
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
            ax.axis("equal")  # Đảm bảo Pie Chart là hình tròn

            st.write("### Biểu đồ Pie Chart")
            st.pyplot(fig)
        else:
            st.warning("Dữ liệu không có đủ cột danh mục hoặc số để vẽ biểu đồ tròn.")
