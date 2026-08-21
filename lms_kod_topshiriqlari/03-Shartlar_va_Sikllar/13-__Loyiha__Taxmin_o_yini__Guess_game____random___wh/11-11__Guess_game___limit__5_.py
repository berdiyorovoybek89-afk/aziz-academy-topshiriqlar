# Yashirin son = 10
# 5 ta urinish beriladi.
# Oxirida yutqazsa "You lost" chiqaring.
secret = 10
tries = 5
won = False
for _ in range(tries):
    guess = int(input())
    if guess == secret:
        print("Correct")
        won = True
        break
if not won:
    print("You lost")
        