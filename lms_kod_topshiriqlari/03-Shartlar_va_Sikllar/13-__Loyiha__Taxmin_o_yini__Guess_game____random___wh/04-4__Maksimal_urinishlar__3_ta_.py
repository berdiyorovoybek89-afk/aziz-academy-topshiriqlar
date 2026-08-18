# Yashirin son = 8
# Foydalanuvchiga maksimal 3 ta urinish beriladi.
# Agar topa olmasa "Game Over" chiqaring.
for _ in range(3):
    if int(input()) == 8:
        print("Correct")
        break
else:
    print("Game Over")