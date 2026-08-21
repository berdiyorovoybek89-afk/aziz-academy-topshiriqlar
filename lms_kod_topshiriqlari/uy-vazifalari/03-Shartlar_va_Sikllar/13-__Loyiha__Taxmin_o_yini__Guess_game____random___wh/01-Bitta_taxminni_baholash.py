secret = int(input())
guess = int(input())
if guess > secret:
    print("KATTA")
elif guess < secret:
    print("KICHIK")
else:
    print("TOPDINGIZ")