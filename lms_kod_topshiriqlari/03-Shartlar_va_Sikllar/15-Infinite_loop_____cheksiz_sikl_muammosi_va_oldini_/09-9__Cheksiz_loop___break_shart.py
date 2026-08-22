import sys
for line in sys.stdin.read().split():
    n = int(line)
    if n < 0:
      break
    print(n)