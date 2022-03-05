"""
한 개의 문자열이 주어지면 문자열의 각 문자의 빈도수를 계산하여 빈도수가 가장 큰 문자부
터 차례대로 출력하는 프로그램을 작성하세요.
단 대소문자를 구분합니다.

"""
import collections
def solution(s):
    answer = 0
    a = collections.Counter(s)
    # for i in range(1,len(a))
    print(a)
    answer = ""
    for i in range(len(a)):
        # print(a.most_common(len(a))[i][0])
        answer +=a.most_common(len(a))[i][0]*a.most_common(len(a))[i][1]
    # ,key= a.most_common(1))
    print(a.most_common(5)[1][0])
    print(a.most_common(5))
    print(a.most_common(1)[0][0])
    print(answer)

    return answer

if solution("aaAAcccbbbBB") == 'cccbbbAABBaa':
    print('정답')
else:
    print('틀렸음')