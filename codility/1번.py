
A = [2, 1, 3, 5, 4]
A = [1,2,3,4,5]


def solution(A):
    answer = 0
    # 1번부터 차례대로 연결 될 때만 빛이 난다.
    # 배열까지 더했을 때 그 합이 같다면 빛이 난다는 뜻
    # 그리고 answer += 1해주면 된다.
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        num = i+1
        print(sum, num )
        if num % 2 == 0:
            if sum == (num + 1) * (num//2):
                answer += 1
        elif num % 2 != 0:
            if sum == num * ((num+1) // 2):
                answer += 1


    return answer

print(solution(A))