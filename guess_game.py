
def check_guess(secret, guess):
    if guess == secret:  # Toán tử so sánh
        return "Đúng"
    elif guess < secret:
        return "Nhỏ hơn"
    else:
        return "Lớn hơn"

secret_number = 5
max_attempts = 10
attempts = 0

while attempts < max_attempts:  # Vòng lặp while
    try:
        guess = int(input("Hãy đoán số (1-10): "))  # Chuyển đổi kiểu dữ liệu
        result = check_guess(secret_number, guess)
        print(result)
        if result == "Đúng":
            print(f"Chúc mừng! Bạn đoán đúng sau {attempts + 1} lần.")
            break
        attempts += 1
    except ValueError:
        print("Vui lòng nhập số nguyên!")
    
if attempts == max_attempts:
    print("Bạn đã hết lượt đoán! Số bí mật là", secret_number)