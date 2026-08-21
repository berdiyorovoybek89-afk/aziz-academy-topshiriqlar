# Yashirin son = -4
# Katta/kichik tekshiruvi manfiy sonlar bilan ham ishlasin.
secret = -4
g1 = int(input())
if g1 == secret:
    print("Correct")
else:
    print("Low" if g1 < secret else "High")
    g2 = int(input())
    print("Correct" if g2 == secret else "Wrong")