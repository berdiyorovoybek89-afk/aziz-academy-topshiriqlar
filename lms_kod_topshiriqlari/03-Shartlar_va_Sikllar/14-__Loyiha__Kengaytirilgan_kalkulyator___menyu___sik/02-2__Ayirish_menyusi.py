import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = int(data[1])
    tanlov = int(data[2])
    if tanlov == 2:
        print(a - b)