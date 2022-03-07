"""

1000 70 170
고정비용 가변비용 판매가격
판매가격>고정비용+가변비용이 되는 손익분기점을 출력
"""
A,B,sale = map(int,input().split())
if B>=sale:
    print(-1)
else:
    cnt = A//(sale-B)
    print(cnt+1)
