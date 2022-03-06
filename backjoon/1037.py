"""
https://www.acmicpc.net/problem/1037
6
3 4 2 12 6 8
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
한자리수중 가능한 경우의 수는 4와 9가 있다. 이들은 2*2와 3*3이므로 값을 2번 곱하면 된다.
두자리는 가장 작은숫자와 가장큰숫자를 곱하면 값이 나온다.
"""
import sys
input = lambda : sys.stdin.readline()
N = int(input())
lst = list(map(int,input().split()))
if N<1:
    print(lst[0]*lst[0])
else:
    print(min(lst) * max(lst))


