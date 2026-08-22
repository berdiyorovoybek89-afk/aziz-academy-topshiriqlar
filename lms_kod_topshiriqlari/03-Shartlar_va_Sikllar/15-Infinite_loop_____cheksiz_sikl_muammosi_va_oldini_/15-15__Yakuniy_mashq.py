import sys
data = sys.stdin.read().split()
if data:
  if data[0] == "hello":
    print("Working")
  else:
    n = int(data[0])
    lst = [int(x) for x in data[1:]]
    print(lst[0])
    if len(lst) > 2:
     print(lst[1:-1])
    print(lst[-1])