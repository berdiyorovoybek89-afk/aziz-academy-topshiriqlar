# Yashirin son = 6
# Agar foydalanuvchi 1..10 dan tashqari son kiritsa "Invalid" chiqaring (urinish sanalmaydi).
while True:
    n = int(input())
    if 1 <= n <= 10:
        if n == 6:
            print("Correct")
            break
    else:
        print("Invalid")