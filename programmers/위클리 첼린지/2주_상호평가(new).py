a = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

answer = ''
student_score = list(map(list,zip(*a)))
# 등급 함수화
def grade(average):
    if average>=90:
        answer = 'A'
    elif average>=80:
        answer = 'B'
    elif average>=70:
        answer = 'C'
    elif average>=50:
        answer = 'D'
    else:
        answer = 'F'
    return answer
for index,score in enumerate(student_score):
    # 1.최저값과 최대값을 찾고 유일한 값인지 확인
    # if min(score) == score[index] or max(score) == score[index]:
    #     if score.count(score[index])==1:
    #         score.remove(score[index])

    # 2.자신값 저장 후 정렬하여 최저값과 최대값 확인 후 2번째와 뒤에서 2번째부터로 재정의
    mine = score[index]
    score.sort()
    if score[0] == mine and score[0] != score[1]:
        score=score[1:]
    elif score[len(score)-1] != mine and score[len(score)-2] == mine:
        score=score[:-1]


    average = sum(score)/len(score)
    answer +=grade(average)

    print(score)
print(answer)