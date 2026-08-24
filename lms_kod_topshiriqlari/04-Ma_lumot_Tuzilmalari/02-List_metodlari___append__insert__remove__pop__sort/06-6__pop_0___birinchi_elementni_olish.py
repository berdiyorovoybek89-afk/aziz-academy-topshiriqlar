# n = int(input())
# lst = list(map(int, input().split()))
# Birinchi elementni pop(0) qiling va chiqar.
# Keyin listni chiqar.
n = int(input())
lst = list(map(int, input().split()))
popped_val = lst.pop(0)
print(popped_val)
print(lst)