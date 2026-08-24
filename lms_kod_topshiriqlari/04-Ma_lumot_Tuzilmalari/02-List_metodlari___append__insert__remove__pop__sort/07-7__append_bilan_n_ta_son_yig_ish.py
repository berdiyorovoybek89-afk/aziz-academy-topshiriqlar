# n va n ta son beriladi.
# Bo‘sh list yarating va hammasini append bilan qo‘shing.
# Oxirida listni chiqaring.
n = int(input())
sonlar = list(map(int, input().split()))
lst = []
for x in sonlar:
    lst.append(x)
print(lst)