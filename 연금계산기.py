"""
국민연금은 연기한 금액만큼 이자를 준다.
1년 연기에 7.2% 최대5년 36%를 추가로 지급함
연기는 금액의 50~100%까지 가능하다.
연금예상금액과 몇년간 연금을 받을 수 있을지 입력하면
연기 금액이 0, 50,60,70,80,90,100%일 때 총 수령금액을 알 수 있게 출력한다.
출력은 1년 평균 받는 금액, 총금액
세금은 5.41%를 기준으로 한다.
물가상승분은 1.5%기준으로 한다.
"""
"""
복잡한거 다빼고 연금받는액수가 148만원일때 50%받고 안받고 차이
5년 8880 vs 4440으로시작함
"""
A = 88800000
B = 44400000
cnt = 0
while A>B:
    cnt+=1
    A = A+1480000
    B = B + 1746400
print(f'{A},{B},{cnt}달,{cnt//12}년' )
exit()
tax = 0.0541 #세금 현재 받는것에서 세금으로 나가는 것 5.41%
inflation_rate = 0.015 #물가상승률 단리로 붙어서 준다. 1.5%
print("한달 연금예상금액 : ",end='')
N = int(input())
N = N*12 #1년에 받는 연금
answer = 0

# 연금 계산기 매년 받는 연금액 : 연금액*12*물가상승률-세금
# N*12*inflation_rate-N*12*inflation_rate*(tax/100) #그냥 바로 받는 사람
def calc(N,L,sum):
    global answer
    if L==i:
        # print(sum,end='')
        answer = round(sum)
        # print(N,L,sum)
        return
    else:
        calc(N,L+1,sum+N+N*inflation_rate-(N+N*inflation_rate)*tax)
def calc_per(L,sum,per): # 여기는 6년부터 계산함
    global answer
    if L==i:
        return sum
    calc(round(N*per/100),5,0)
        
        
delay = [0,50,60,70,80,90,100]
print("연기 금액 퍼센트",'0','50','60','70','80','90','100')
for i in range(5):
    print(i,'년차 연금',calc(N,0,0),answer)

    # print(i,'년차 연금',calc(0,0),calc_per(0,0,50) )







