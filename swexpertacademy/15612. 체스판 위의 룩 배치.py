T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = "yes"
    temp = []
    for i in range(8):
        arr = input()
        cnt = 0
        for index,a in enumerate(arr):
            if 'O' == a:
                temp.append(index+1)
                cnt +=1
            if cnt >= 2:
                answer = "no"
    if sum(temp) != 36:
        answer = "no"
    print("#{0} {1}".format(test_case, answer))