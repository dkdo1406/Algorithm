from collections import defaultdict
import random
class RandomizedCollection:

    def __init__(self):
        global dic, arr
        dic = defaultdict(set)
        arr = []

    def insert(self, val: int) -> bool:
        global dic, arr
        if val in dic:
            arr.append(val)
            dic[val].add(len(arr)-1)
            return False
        else:
            arr.append(val)
            dic[val].add(len(arr)-1)
            return True

    def remove(self, val: int) -> bool:
        global dic, arr
        if val in dic:
            if val == arr[-1]:
                arr.pop()
                dic[val] -= {len(arr)}
            else:
                number = dic[val].pop()
                dic[arr[-1]] -= {len(arr)-1}
                dic[arr[-1]].add(number)
                arr[-1], arr[number] = arr[number], arr[-1] 
                arr.pop()
            if len(dic[val]) == 0:
                dic.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        global dic, arr
        return random.choice(arr)
        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()