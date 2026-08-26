# n va n ta son beriladi.
# Listning ikkinchi yarmini slicing bilan chiqaring.
# (Agar toq bo‘lsa, o‘rtadagi kirmasin)
n = int(input())
lst = list(map(int, input().split()))
mid = (n + 1) // 2
print(lst[mid:])