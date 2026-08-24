# n = int(input())
# lst = list(map(int, input().split()))
# Oxirgi elementni pop qiling va chiqar.
# Keyin qolgan listni ham chiqar.
n = int(input())
lst = list(map(int, input().split()))
popped_val = lst.pop()
print(popped_val)
print(lst)