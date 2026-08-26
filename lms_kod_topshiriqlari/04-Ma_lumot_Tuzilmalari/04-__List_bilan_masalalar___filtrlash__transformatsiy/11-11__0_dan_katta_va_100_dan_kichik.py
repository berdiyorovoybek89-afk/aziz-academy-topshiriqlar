# n va n ta son beriladi.
# 0 < x < 100 bo‘lgan sonlarni chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x for x in numbers if 0 < x < 100]
print(result)