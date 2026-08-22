# n = int(input())
# skip = int(input())
# 1..n, skip ni tashlab keting (continue).
import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    skip = int(data[1])
    for i in range(1, n + 1):
        if i == skip:
            continue
        print(i)