from collections import deque
from collections import defaultdict
A = [15, 13, 5, 7, 4, 10, 12, 8, 2, 11, 6, 9, 3]

def LongestIncreasingSubsequence(seq):
    smallest_end_value = [None] * (len(seq)+1)
    smallest_end_value[0] = -1
    lic_lenght = 0

    for i in range(len(seq)):
        lower = 0
        upper = lic_lenght

        while lower <= upper:
            mid = (upper + lower) //2
            print(lower, upper, mid)
            if seq[i] < smallest_end_value[mid]:
                upper = mid - 1
            elif seq[i] > smallest_end_value[mid]:
                lower = mid + 1

        if smallest_end_value[lower] == None:
            smallest_end_value[lower] = seq[i]
            lic_lenght += 1
        else:
            smallest_end_value[lower] = min(smallest_end_value[lower], seq[i])

    return lic_lenght


def solution(A):
    answer = 0

    # 2번까지 방향전환 가능
    # 최대한 많은 코스를 거쳐가라
    # 언제나 현재 위치에서 작은값 또는 큰 값으로 갈 수 있다.
    multiverse = []
    bound = max(A) + 1
    for point in A:
        multiverse.append(bound * 2 + point)
        multiverse.append(bound * 2 - point)
        multiverse.append(point)


    print(multiverse)
    answer = LongestIncreasingSubsequence(multiverse)



    return answer





print(solution(A))