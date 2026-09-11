import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
    for i in range(1, n * 2 + 1, 2):
        print(int(data[i]) + int(data[i + 1]))