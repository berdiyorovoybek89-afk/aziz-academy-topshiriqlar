numbers = input().split()
k = int(input())
numbers.pop(k)
print(*(numbers))