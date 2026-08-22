# n = int(input())
# while i<n.
# i ni o'zgartirib loopni to'g'ri qiling.
import sys
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    i = 0
    while i < n:
      print(i)
      i += 1