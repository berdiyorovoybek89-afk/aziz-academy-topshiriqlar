# Bo‘sh list bilan boshlang.
# Qatorlarda buyruqlar keladi (hammasi lowercase):
# append x
# insert i x
# remove x
# pop i
# stop
# stop kelganda listni chiqaring.
# Eslatma: remove x bo‘lsa va x topilmasa, hech narsa qilmang.
import sys
lst = []
for line in sys.stdin:
    c, *a = line.split()
    if c == "stop": break
    elif c == "append": lst.append(int(a[0]))
    elif c == "insert": lst.insert(int(a[0]), int(a[1]))
    elif c == "remove" and int(a[0]) in lst: lst.remove(int(a[0]))
    elif c == "pop" and 0 <= int(a[0]) < len(lst): lst.pop(int(a[0]))
print(lst)