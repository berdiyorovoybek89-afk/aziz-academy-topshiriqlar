# Yashirin son = 7
# Foydalanuvchi son kiritadi.
# Agar kichik bo‘lsa "Low", katta bo‘lsa "High", teng bo‘lsa "Correct" chiqar va to‘xtat.
while True:
    n = int(input())
    print("Low" if n < 7 else ("High" if n > 7 else "Correct"))
    if n == 7:
        break