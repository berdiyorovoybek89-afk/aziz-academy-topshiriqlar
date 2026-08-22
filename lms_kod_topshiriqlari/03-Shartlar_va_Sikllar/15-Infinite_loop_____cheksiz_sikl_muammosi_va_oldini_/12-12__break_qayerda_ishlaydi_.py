import sys
data = sys.stdin.read().split()
if data:
  n = int(data[0])
  break_at = int(data[1])
  for i in range(1, n + 1):
     if i == break_at:
       break            
     print(i)