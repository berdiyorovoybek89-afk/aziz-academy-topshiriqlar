# Ikki son va tanlov beriladi.
# Agar tanlov 3 bo‘lsa, a*b ni chiqaring.
import sys
data = sys.stdin.read().split()
if data:
    a = int(data[0])
    b = int(data[1])
    tanlov = int(data[2])
    if tanlov == 3:
        print(a * b)