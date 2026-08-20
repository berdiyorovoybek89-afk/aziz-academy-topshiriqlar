while True:
    try:
        n = int(input())
        if n == 0:
            print("Exit")
            break
        elif n == 3:
            print("Correct")
        elif n < 3:
            print("Low")
        else:
            print("High")
    except EOFError:
        break