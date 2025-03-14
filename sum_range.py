def sum_range(a, b):
    total = 0
    for i in range(a, b + 1):  # Vòng lặp for
        total += i
    return total

try:
    a = int(input("Nhập số a: "))  # Chuyển đổi kiểu dữ liệu
    b = int(input("Nhập số b: "))
    if a >= b:  # Toán tử so sánh
        print("a phải nhỏ hơn b!")
    else:
        result = sum_range(a, b)
        print(f"Tổng các số từ {a} đến {b} là: {result}")

except ValueError:
    print("Vui lòng nhập số nguyên!")