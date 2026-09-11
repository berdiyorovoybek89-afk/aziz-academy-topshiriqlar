n = int(input())
data = {}
for _ in range(n):
    key, val = input().split()
    data[key] = int(val)
best_key = max(data, key=data.get)
print(best_key)