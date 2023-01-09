n, m = list(map(int, input().split()))

meetingroom = dict()
for _ in range(n):
    meetingroom[input()] = {i for i in range(9,18)}

def checktime(clock):
    arr = []
    if clock:
        start = clock[0]
        if start == 9:
            start = "09"
        end = clock[0]
        for i in range(1, len(clock)):
            if end + 1 == clock[i]:
                end += 1
            else:
                end += 1
                arr.append(f"{str(start)}-{str(end)}")
                start = clock[i]
                end = clock[i]
        end += 1
        arr.append(f"{str(start)}-{str(end)}")
        canreserve = len(arr)
    else:
        canreserve = "Not"
        print(f"{canreserve} available")
        return
    print(f"{canreserve} available:")
    for i in arr:
        print(i)

def reserve(room, start, end):
    arr = {i for i in range(start, end)}
    meetingroom[room] -= arr

for _ in range(m):
    room, start, end = list(input().split())
    reserve(room, int(start), int(end))


meetingroom = sorted(meetingroom.items())
endroom = meetingroom[-1][0]
for room, clock in meetingroom:
    print(f"Room {room}:")
    checktime(list(clock))
    if room != endroom:
        print("-----")