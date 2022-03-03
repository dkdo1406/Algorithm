"""
https://programmers.co.kr/learn/courses/30/lessons/17684
https://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.
사전안에 없는 문자가 나올때까지 rt를 증가시킨다.
사전에 없는 문자가 나오면 lt:rt-1문자를 사전에서 찾아 결과값에 추가하고 lt:rt는 사전에 추가한다.
KAKAO	[11, 1, 27, 15]
TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
ABABABABABABABAB	[1, 2, 27, 29, 28, 31, 30]

슬라이드윈도우 사용하면 되는 문제, lt와 rt
"""

msg = 'ABABABABABABABAB'
answer = []
lt=0
rt=0

alpha = [0]
for i in range(65,91):
    alpha.append(chr(i))

while True:
    rt+=1
    if rt==len(msg)+1:
            answer.append(alpha.index(msg[lt:rt-1]))
            break
    if msg[lt:rt] not in alpha: #rt가 마지막 위치면 출력하고 마무리하면 될듯
        print(msg[lt:rt-1])
        answer.append(alpha.index(msg[lt:rt-1]))   #alpha의 index를 넣어야 한다.
        alpha.append(msg[lt:rt])
        lt=rt-1
        rt=lt
    
print(answer)