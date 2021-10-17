a = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
answer = ''
ismine = 0
for i in range(0,len(a)): # 자기자신에게 투표한 아이
    save = []
    for j in range(0,len(a)):
        if i==j:
            ismine = a[i][i]
        save.append(a[j][i])
    # 첫번째 자기자신에게 작성한 점수가 최고점인지 최저점인지 확인
    # 유일한지 아닌지 확인 유일하다면 삭제 후 평균 계산
    if ismine is max(save) or ismine is min(save):
        if save.count(ismine) ==1:
            save.remove(ismine)
    average = sum(save)/len(save)
    if average >=90:
        answer += 'A'
    elif average >=80 and average<90:
        answer += 'B'
    elif average >=70 and average<80:
        answer += 'C'
    elif average >=50 and average<70:
        answer += 'D'
    elif average<50:
        answer += 'F'

    print(save)
print(answer)
