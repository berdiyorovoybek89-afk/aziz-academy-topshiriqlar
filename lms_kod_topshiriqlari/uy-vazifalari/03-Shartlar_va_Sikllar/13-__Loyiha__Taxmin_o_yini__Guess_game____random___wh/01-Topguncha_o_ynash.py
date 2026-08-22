import sys
s = list(map(int, sys.stdin.read().split()))
x, g = s[0], s[1:]
for i, v in enumerate(g, 1):
    print(
        "KATTA" if v > x else ("KICHIK" if v < x else f"TOPDINGIZ\nUrinishlar: {i}")
    )
    if v == x:
        break