input = "5 8 3" # N,M,K     K는 항상 M 보다 작거나 같다.
input2 = "2 4 5 4 6"
result = 0
N,M,K = map(int,input.split(" "))
input2_split = list(map(int,input2.split(" ")))
# N  두번째줄 총 개수
# M  총 더할 개수
# K  최대값 제한

input2_split.sort()
first_num = input2_split[-1]
second_num = input2_split[-2]
result = first_num * (M-M//K)
result += second_num * (M//K)

print(result)


