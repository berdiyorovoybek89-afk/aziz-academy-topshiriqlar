# n va n ta son beriladi.
# Har bir sonning kvadratidan iborat list chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [x ** 2 for x in numbers]
print(result)