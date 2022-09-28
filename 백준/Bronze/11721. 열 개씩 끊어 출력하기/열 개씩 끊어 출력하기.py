import sys
import math
input = lambda: sys.stdin.readline().rstrip()
a = list(input())
if len(a) < 10:
    print(''.join(a))
else:
    for i in range(math.ceil(len(a) / 10)):
        print(''.join(a[i*10:(i+1)*10]))