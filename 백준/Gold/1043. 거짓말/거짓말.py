from collections import deque
N, M = list(map(int, input().split()))
know_true = list(map(int, input().split()))
parties = deque()
for i in range(M):
    arr = list(map(int, input().split()))
    parties.append(set(arr[1:]))

know = set(know_true[1:])
q = deque(know_true)
q.popleft()
while q:
    iKnow = q.popleft()
    temp = set()
    for _ in range(M):
        party = parties.popleft()
        if iKnow in party:
            temp.update(party)
            M -= 1
            continue

        parties.append(party)
    aa = temp - know
    know.update(aa)
    if aa:
        q.extend(list(aa))

print(M)

