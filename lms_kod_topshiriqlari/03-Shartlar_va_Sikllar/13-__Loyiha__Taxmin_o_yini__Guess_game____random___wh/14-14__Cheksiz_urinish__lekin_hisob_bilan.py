# Yashirin son = 11
# Cheksiz urinish.
# Oxirida faqat urinishlar sonini chiqaring.
secret = 11
count = 0
while True:
    guess = int(input())
    count += 1
    if guess == secret:
        print(count)
        break