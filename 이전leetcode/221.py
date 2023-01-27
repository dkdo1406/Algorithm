"""
https://leetcode.com/problems/maximal-square/
최대 정사작형의 크기를 구하라
dp문제임
11
11 일경우 오른쪽밑에것을 기준으로
"""
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
if matrix is None or len(matrix)<1:
    print("없다")

row,col = len(matrix),len(matrix[0])
dp = [[0]*(col+1) for i in range(row+1)]
answer = 0
for r in range(row):
    for c in range(col):
        if matrix[r][c]=='1':
            for i in dp:
                print(i)
            print()
            dp[r+1][c+1]=min(dp[r][c],dp[r+1][c],dp[r][c+1])+1 #1을 한칸뒤에넣어서 확인하는 것
            answer = max(answer,dp[r+1][c+1])
print(answer*answer)