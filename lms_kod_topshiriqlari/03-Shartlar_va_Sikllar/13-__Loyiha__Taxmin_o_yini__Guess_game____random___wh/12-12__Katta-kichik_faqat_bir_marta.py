# Yashirin son = 8
# Birinchi urinishda faqat yordam beriladi.
# Keyingisida faqat Correct yoki Wrong.
s = 8
g1 = int(input())
if g1 == s:
    print("Correct")
else:
    print("Low" if g1 < s else "High")
    g2 = int(input())
    print("Correct" if g2 == s else "Wrong")