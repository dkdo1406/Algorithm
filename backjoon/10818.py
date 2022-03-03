"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
5
20 10 35 30 7
"""
import sys
input = lambda : sys.stdin.readline()

n = int(input())
lst = list(map(int,input().split(' ')))
print(min(lst),max(lst))