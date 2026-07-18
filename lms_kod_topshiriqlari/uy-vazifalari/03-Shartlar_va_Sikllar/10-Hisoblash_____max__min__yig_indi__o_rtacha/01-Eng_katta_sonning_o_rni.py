N = int(input())
birinchi_son = int(input())
eng_katta = birinchi_son
eng_katta_orin = 1
for i in range(2, N + 1):
    son = int(input())
    if son > eng_katta:
        eng_katta = son
        eng_katta_orin = i
print(eng_katta_orin)