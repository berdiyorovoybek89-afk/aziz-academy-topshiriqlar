from collections import Counter
n = int(input())
words = [input() for _ in range(n)]
print(Counter(words).most_common(1)[0][0])