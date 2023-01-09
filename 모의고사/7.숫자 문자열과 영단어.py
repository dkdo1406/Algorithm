s = "one4seveneightone"
# result = 1478
dict = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7",
        "eight":"8","nine":"9"}
for i in dict:
    # print(dict[i])
    s = s.replace(i,dict[i])
print(s)

