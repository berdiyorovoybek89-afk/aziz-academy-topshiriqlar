import sys
count = 0
for line in sys.stdin.read().split():
    if int(line) < 0:
        break
    count += 1
print(count)