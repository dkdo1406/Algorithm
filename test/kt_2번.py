def solution(n, info):
    global answer,flag
    answer = 100000
    flag = False
    visited = [False]*(n+1)
    visited[1]=True
    def DFS(S,time,visited): # S:출발점, dis: 이전점 거리, time: 총시간
        global answer,flag

        print(visited,S,time)
        if S==n: # 종점에 도착하면 총 시간 저장
            answer = min(answer,time)
            flag = True
            return
        else:
            for start,end,dis in info:
                if start == S and not visited[end]:

                    if time==0 or time%(2*dis)==0:
                        DFS(end,time+dis,visited) #다시오는 시간까지 같이 저장
                    else:
                        DFS(end,time+time%(2*dis)+dis,visited)
                    visited[end] = False
                elif end == S and not visited[start]:

                    if time==0 or time%dis==0:
                        DFS(start,time+dis,visited)
                    else:
                        DFS(start,time+time%dis+dis,visited)
                    visited[start] = False
    DFS(1,0,visited)
    if flag:
        return answer
    else:
        return -1
n=4
info = [[2,1,4],[2,4,1],[4,3,2],[1,3,2]]
print(solution(n, info))