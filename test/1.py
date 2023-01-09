def solution(n, text, second):
    answer = []
    mongoo = ["_" for i in range(1000)]
    cnt = 0

    # text에 있는것을 mongoo에 넣는다.
    cnt_1 = 0
    while cnt_1<1000:
        for i in range(0, len(text)):
            if text[i] == " ":
                mongoo[cnt_1] = "_"
            else:
                mongoo[cnt_1] = text[i]
            cnt_1 += 1

    ## n+text주기마다 전광판에 넣는다.
    # 1. n>second일 때
    if n>=second:
        for i in range(0,n):
            if i>=n-second:
                answer.append(mongoo[cnt])
                cnt += 1
            else:
                answer.append("_")

    else:
        for i in range(second, second + n):
            answer.append(mongoo[i])

    abc = ''.join(answer)

    print(mongoo)
    print(answer)


    return abc
#n+text마다 반복
n=5 # LED 나타내는 개수
text = "hi bye bye"
second = 5 # 몇초가 지났는가
print(solution(n,text,second))