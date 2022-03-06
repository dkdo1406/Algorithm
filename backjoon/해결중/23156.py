"""
3
10 1.00
11 1.00
12 1.00
타이핑을 하는데 다른사람의 소음을 들으면 타이핑 속도가 낮아진다.
S1 *(1- f1*f2 -... f1*fn)이런식으로 낮아질 때 타이핑 총합이 가장높은값을 출력하라
"""
import sys
input = lambda : sys.stdin.readline()
N = int(input())
for i in range(N):
    G = int(input())
    
    S,noise = map(int,input().split())