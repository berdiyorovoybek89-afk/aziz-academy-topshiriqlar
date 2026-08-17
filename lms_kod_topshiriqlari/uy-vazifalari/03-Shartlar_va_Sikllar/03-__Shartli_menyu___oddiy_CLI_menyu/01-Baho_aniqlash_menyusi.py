m = input()
if m in ("1", "2"):
    b = int(input())
    print("ABCDF"[max(0, 9 - b // 10)] if m == "1" else ("0'tdi" if b >= 60 else "Yiqildi"))