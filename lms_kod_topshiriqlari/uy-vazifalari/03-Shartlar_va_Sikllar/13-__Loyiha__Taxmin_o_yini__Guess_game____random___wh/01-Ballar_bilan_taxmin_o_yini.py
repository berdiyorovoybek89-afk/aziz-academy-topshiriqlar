ball = 100
son = int(input())
while True:
    t = int(input())
    if t == son:
        print("TOPDINGIZ")
        break
    elif t > son:
         print("KATTA")
    else:
        print("KICHIK")
    ball = max(0, ball - 10)
print("Ball:", ball)