"""
https://programmers.co.kr/learn/courses/30/lessons/68644
"""

number = [2,1,3,4,1]
# result = [2,3,4,5,6,7]
result = []
for i in range(0,len(number)-1):
    for j in range(i+1,len(number)):
        result.append(number[i]+number[j])
result.sort()
print(list(set(result)))


