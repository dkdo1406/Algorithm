"""

3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
원의 방정식
(x-a)**2 + (y-b)**2 = r2
여기서 r은 두점간의 거리이다.
r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
r1 + r2 = d 이면 두 원은 외접한다.
|r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
|r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
|r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.

"""
import sys
import math
input = lambda : sys.stdin.readline()

T = int(input())
answer = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int,input().split()))
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 두 원의 거리 (원의방정식활용)
    if distance == 0 and r1 == r2:  # 두 원이 동심원이고 반지름이 같을 때
        answer.append(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
        answer.append(1)
    elif abs(r1 - r2) < distance < (r1 + r2):  # 두 원이 서로다른 두 점에서 만날 때
        answer.append(2)
    else:
        answer.append(0)  # 그 외에
for i in answer:
    print(i)

