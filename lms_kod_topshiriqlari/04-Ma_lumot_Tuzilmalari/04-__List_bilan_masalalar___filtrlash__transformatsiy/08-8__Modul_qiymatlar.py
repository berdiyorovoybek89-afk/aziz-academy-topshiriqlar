# n va n ta son beriladi.
# Har bir sonning modulidan iborat list chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
result = [abs(x)for x in numbers]
print(result)
