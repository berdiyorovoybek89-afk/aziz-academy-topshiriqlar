# n beriladi.
# n ning bo‘luvchilari sonini hisoblab chiqaring.
n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)