"""
2 5 7
N : 노래 곡수
L : 노래 길이
D : 전화 간격 ex) D초마다 1번씩 1초간 벨소리 울림
전화벨소리 들을 수 있는 최소 시간을 구하라
# 노레에는 끝이있지만 벨소리에는 끝이 없다.
# 결국 노래를 모두 구한 후 벨소리를 대입한다. 그값이 없을 경우 노래가 끝나는 시간이 정답이다.

이건 손으로 로직이 어떻게 돌아가는지 그려보고 다시 해보자
"""
import sys
input = lambda : sys.stdin.readline()
input = lambda: sys.stdin.readline()
N,L,D = map(int,input().split())
time = []
count = 0
listen = []
for i in range(1,N+1):
    music = count + L*i
    listen.append(music)
    listen.append(music+1)
    listen.append(music + 2)
    listen.append(music + 3)
    listen.append(music + 4)
    count += 5

ring = 0
while True:
    if ring<=max(listen) and ring in listen:
        print(ring)
        break
    elif ring>max(listen):
        print(ring)
        break
    ring += 1
    ring += D-1