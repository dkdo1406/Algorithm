# from collections import defaultdict
# def solution(id_list, report, k):
#     answer = []
#     # 한번에 한 유저 신고
#     reports = defaultdict()
#     print(report)
#     array = []
#     for c in report:
#         a,b = c.split()
#         if b not in reports[a]:
#             reports[a] += b
#     print(reports)
#     return answer
#
#
# id_list =  ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# print(solution(id_list, report, k))

A,B,N = list(map(int, input().split()))

cnt = 0
result = 0
while cnt < N:
    if A // B == 0:
        result = (A * 10) // B
        A = (A * 10) % B
        cnt += 1
    else:
        result = A // B
        A = A % B
print(result)


