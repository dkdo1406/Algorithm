
A = 6
B = 1
C = 1

def solution(A, B, C):
    answer = ''

    arr = []
    arr.append(['a', A])
    arr.append(['b', B])
    arr.append(['c', C])


    arr.sort(key= lambda x: x[1], reverse= True)

    # 가장 큰 값이 나머지 2개보다 클 경우 개수를 맞춰가며 조합.
    #
    while arr[1][1] + arr[2][1] > 0:

        if answer == '':
            if arr[0][1] > arr[1][1] + arr[2][1]:
                answer += arr[0][0] * 2

                arr[0][1] -= 2
                answer += arr[1][0]
                arr[1][1] -=1
        elif answer[-1] != arr[0][0]:
            if arr[0][1] > arr[1][1] + arr[2][1]:
                if arr[0][1] > 1:
                    answer += arr[0][0]*2

                    arr[0][1] -= 2
                    answer += arr[1][0]
                    arr[1][1] -= 1
            else:
                if arr[0][1] > 1:
                    answer += arr[0][0]
                    arr[0][1] -= 1
                    answer += arr[1][0]
                    arr[1][1] -= 1
        print(arr)
        arr.sort(key=lambda x: x[1], reverse=True)

    if answer[-1] != arr[0][0]:
        if arr[0][1] > arr[1][1] + arr[2][1]:
            if arr[0][1] > 1:
                answer += arr[0][0] * 2
                arr[0][1] -= 2
                answer += arr[1][0]
                arr[1][1] -= 1


    return answer

print(solution(A,B,C))