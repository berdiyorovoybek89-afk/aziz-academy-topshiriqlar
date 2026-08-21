secret = int(input())
k = int(input())
for _ in range(k):
    guess = int(input())
    if guess > secret:
        print("KATTA")
    elif guess < secret:
        print("KICHIK")
    else:
        print("TOPDINGIZ")