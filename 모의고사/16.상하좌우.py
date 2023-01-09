input = 5
input_2 = "R R R U D D"
N = int(input)
me = {"X" : 1,"Y" : 1}
go = input_2.split()

for i in go:
    if i == "R":
        me["Y"] += 1
        if me["Y"]>N:
            me["Y"]=1
    elif i == "L":
        me["Y"] -=1
        if me["Y"]<1:
            me["Y"]=1
    elif i =="U":
        me["X"] -=1
        if me["X"]<1:
            me["X"] = 1
    elif i =="D":
        me["X"] +=1
        if me["X"] >N:
            me["X"] = 1
print(me)