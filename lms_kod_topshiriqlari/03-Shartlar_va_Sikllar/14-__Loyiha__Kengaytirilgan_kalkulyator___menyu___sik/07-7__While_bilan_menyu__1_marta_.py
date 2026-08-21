# while loop: 0 kirguncha har bir sonni chiqar, 0 da Exit
import sys
data = sys.stdin.read().split()
for x in data:
    if x == '0':
        print("Exit")
        break
    else:
        print(x)