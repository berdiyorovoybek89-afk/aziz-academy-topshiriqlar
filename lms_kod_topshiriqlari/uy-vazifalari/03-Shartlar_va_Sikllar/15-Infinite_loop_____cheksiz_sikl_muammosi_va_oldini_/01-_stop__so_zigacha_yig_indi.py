import sys
total = 0
for line in sys.stdin:
    line = line.strip()
    if line == "stop":
        break
    total += int(line)
print(total)