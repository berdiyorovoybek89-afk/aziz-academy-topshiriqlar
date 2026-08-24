import sys
total = 0
for x in sys.stdin.read().split():
    if x == '0':
        break
    total += int(x)
print(total)