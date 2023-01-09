# arr1 = [[1],[2]]
# arr2 = [[3],[4]]
# # result = [[4],[6]]
# result = arr1
# for i in range(len(arr1)):
#     for j in range(len(arr1[i])):
#         print(i,j)
#         result[i][j]=arr1[i][j]+arr2[i][j]
# print(result)

#다른 풀이
arr1 = [[1],[2]]
arr2 = [[3],[4]]
# result = [[4],[6]]

result = [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]
print(result)
