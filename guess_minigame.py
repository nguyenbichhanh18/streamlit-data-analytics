import random

def check_guess(secret_number, user_guess):
    if user_guess < secret_number:
        return "Lớn hơn"
    elif user_guess > secret_number:
        return "Nhỏ hơn"
    else:
        return "Chúc mừng! Bạn đã đoán đúng."

def guess_minigame():
    secret_number = random.randint(1, 100)  # Số bí mật từ 1 đến 100
    attempts = 10

    print("Chào mừng bạn đến với trò chơi đoán số!")
    print("Bạn có 10 lần đoán để tìm ra số bí mật từ 1 đến 100.")

    for attempt in range(attempts):
        try:
            user_guess = int(input(f"Nhập số bạn đoán (Lần đoán {attempt + 1}/{attempts}): "))
            if user_guess < 1 or user_guess > 100:
                print("Vui lòng nhập số từ 1 đến 100!")
                continue
                
            result = check_guess(secret_number, user_guess)
            print(result)
            if result == "Chúc mừng! Bạn đã đoán đúng.":
                break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
            continue
    else:
        print(f"Bạn đã hết lượt đoán. Số bí mật là {secret_number}.")

if __name__ == "__main__":
    guess_minigame()