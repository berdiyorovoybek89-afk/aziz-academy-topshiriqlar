import sys
data = sys.stdin.read().split()
if data:
    target, n = int(data[0]), int(data[1])
    won = False
    for i in range(2, 2 + n):
        x = int(data[i])
        if x == target:
            print("TOPDINGIZ")
            won = True
            break
        elif x < target:
            print("KICHIK")
        else:
            print("KATTA")
    if not won:
        print("YUTQAZDINGIZ")