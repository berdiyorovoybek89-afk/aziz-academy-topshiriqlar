# n va n ta son beriladi.
# Bo‘sh list yarating.
# Har bir sonni listning boshiga insert(0, x) qilib qo‘shing.
# Natijada list teskari bo‘lib chiqadi.
# Listni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
res = []
for x in sonlar:
    res.insert(0, x)
print(res)