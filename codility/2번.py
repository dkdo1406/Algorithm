
S = 'aabbcc'
C = [1, 2, 1, 2, 1, 2]
def solution(S, C):
    temp = S[0]
    saveIndex = 0
    answer = 0
    cnt = 1
    for index, i in enumerate(S):
        if index != 0:
            if i == temp:
                cnt += 1
            else:
                if cnt > 1:
                    answer += sum(C[saveIndex:saveIndex+cnt]) - max((C[saveIndex:saveIndex+cnt]))
                temp = i
                saveIndex = index
                cnt = 1
    if cnt > 1:
        answer += sum(C[saveIndex:saveIndex+cnt]) - max((C[saveIndex:saveIndex+cnt]))

    return answer



print(solution(S, C))