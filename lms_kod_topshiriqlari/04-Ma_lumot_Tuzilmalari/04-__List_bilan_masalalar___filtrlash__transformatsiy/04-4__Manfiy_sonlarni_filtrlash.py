# n va n ta son beriladi.
# Faqat manfiy sonlarni chiqaring.
n = int(input())
numbers = list(map(int, input().split()))
negative_numbers = [x for x in numbers if x < 0]
print(negative_numbers)
