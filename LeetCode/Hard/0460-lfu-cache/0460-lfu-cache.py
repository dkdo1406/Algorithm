from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        global cache, memory, freq
        memory = capacity
        cache = defaultdict(list)
        freq = collections.OrderedDict()
        
    def get(self, key: int) -> int:
        global cache, freq
        if key not in cache:
            return -1
        else:
            seq = cache[key][1]
            if len(freq[seq]) == 1:
                freq.pop(seq)
            else:
                freq[seq].remove(key)
            if seq+1 in freq:
                freq[seq+1] += [key]
            else:
                freq[seq+1] = [key]
            cache[key][1] += 1

            arr = list(freq.items())
            arr.sort(key = lambda x: x[0])
            freq = collections.OrderedDict(arr)
            return cache[key][0]

    def put(self, key: int, value: int) -> None:
        global cache, memory, freq
        if memory > 0:
            if key in cache:
                seq = cache[key][1]
                if len(freq[seq]) == 1:
                    freq.pop(seq)
                else:
                    freq[seq].remove(key)
                if seq+1 in freq:
                    freq[seq+1] += [key]
                else:
                    freq[seq+1] = [key]
                cache[key][1] += 1
                cache[key][0] = value
            else:
                if len(cache) == memory:
                    for i, j in freq.items():
                        pop_elem = j[0]
                        if len(freq[i]) == 1:
                            freq.pop(i)
                        else:
                            freq[i].remove(pop_elem)
                        cache.pop(pop_elem)
                        break
                cache[key] = [value, 1]
                if 1 in freq:
                    freq[1] += [key]
                else:
                    freq[1] = [key]

            arr = list(freq.items())
            arr.sort(key = lambda x: x[0])
            freq = collections.OrderedDict(arr)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)