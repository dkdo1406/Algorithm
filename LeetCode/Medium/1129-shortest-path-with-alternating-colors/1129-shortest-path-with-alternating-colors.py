class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_ans = [-1 for _ in range(n)]
        blue_ans = [-1 for _ in range(n)]
        redgraph = [[] for _ in range(n)]
        bluegraph = [[] for _ in range(n)]
        for i, j in redEdges:
            redgraph[i].append(j)
            
        for i, j in blueEdges:
            bluegraph[i].append(j)

        def dfs(L, end, color):
            if color == "blue":
                red_ans[end] = L
                if bluegraph[end]:
                    for start in bluegraph[end]:
                        if blue_ans[start] == -1 or blue_ans[start] > L + 1:
                            dfs(L + 1, start, "red")
            if color == "red":
                blue_ans[end] = L
                if redgraph[end]:
                    for start in redgraph[end]:
                        if red_ans[start] == -1 or red_ans[start] > L + 1:
                            dfs(L + 1, start, "blue")
            
        if redgraph[0]:
            for i in redgraph[0]:
                dfs(1, i, "blue")
        
        if bluegraph[0]:
            for i in bluegraph[0]:
                dfs(1, i, "red")
        ans = []
        red_ans[0] = 0
        blue_ans[0] = 0
        for i in range(n):
            if red_ans[i] == -1 or blue_ans[i] == -1:
                ans.append(max(red_ans[i], blue_ans[i]))
            else:
                ans.append(min(red_ans[i], blue_ans[i]))
        return ans