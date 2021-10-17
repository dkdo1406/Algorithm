N= 5
stages = [4,4,4,4,4]
# N=5
# stages =[2, 1, 2, 6, 2, 4, 3, 3]

# N 전체 스테이지의 개수
# stages 사용자가 현재 멈춰있는 스테이지의 번호
# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 실패율이 낮은순서대로 스테이지 출력

# come_to_stage 제거, total==0을 개선한 코드
answer = []
fail={}
stages.sort()

total = len(stages)

for i in range(1,N+1):
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    if total ==0: #total이 0이라는 뜻은 스테이지 도달 플레이어 수 - 클리어하지 못한 플레이어수가 0이다.
        fail[i]=0  # 즉 다음 N이 있는데 도달하지 못한 경우임 그래서 continue를 하면 안되고 0을 넣어줘야 한다.
        # continue
    else:
        fail[i] = (stages.count(i) / total)
    total-=stages.count(i)

fail = sorted(fail.items(), reverse=True, key=lambda x:x[1])

for i,j in fail:
    answer.append(i)
print(fail)
print(answer)


# 런타임에러난 코드

# answer = []
# fail={}
# for i in range(1,N+1):
#     come_to_stage = []
#     for j in stages:
#         if i<=j:
#             come_to_stage.append(j)
#     fail[i]=(come_to_stage.count(i)/len(come_to_stage))
# fail = sorted(fail.items(), reverse=True, key=lambda x:x[1])
# for i,j in fail:
#     answer.append(i)
# print(answer)






