class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        Radiant = deque()
        Dire = deque()
        for index in range(len(senate)):
            q.append(index)
            if senate[index] == "R":
                Radiant.append(index)
            else:
                Dire.append(index)
        ban = set()
        while q:
            n = len(q)
            for _ in range(n):
                index = q.popleft()
                if index in ban:
                    continue
                if senate[index] == "R":
                    if not Dire:
                        return "Radiant"
                    
                    i = Radiant.popleft()
                    while i != index:
                        i = Radiant.popleft()
                    Radiant.append(i)
                    ban.add(Dire.popleft())
                    q.append(index)
                else:
                    if not Radiant:
                        return "Dire"
                    i = Dire.popleft()
                    while i != index:
                        i = Dire.popleft()
                    Dire.append(i)
                    ban.add(Radiant.popleft())
                    q.append(index)
                        

                    

        