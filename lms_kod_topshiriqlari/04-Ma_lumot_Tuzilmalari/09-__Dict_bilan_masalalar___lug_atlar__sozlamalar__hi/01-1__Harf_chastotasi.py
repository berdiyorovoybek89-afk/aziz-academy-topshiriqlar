s = input()
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(*(f"{k}:{v}" for k, v in d.items()))