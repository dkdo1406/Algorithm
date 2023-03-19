class WordDictionary:

    def __init__(self):
        self.dic = dict()
        self.words = set()
        self.lengths = set()

    def addWord(self, word: str) -> None:
        add_dic = self.dic
        self.words.add(word)
        self.lengths.add(len(word))
        for i in word:
            if "." not in add_dic:
                add_dic["."] = []

            if i not in add_dic:
                add_dic[i] = dict()
                add_dic["."].append(i)
            add_dic = add_dic[i]
        add_dic["*"] = ""

    def search(self, word: str) -> bool:
        if len(word) not in self.lengths:
            return False
        elif "." not in word:
            return word in self.words
        else:
            search_dic = self.dic
            q = deque()
            q.append((0, search_dic))
            while q:
                index, search_dic = q.popleft()
                if index == len(word):
                    if "*" in search_dic:
                        return True
                    continue
                if word[index] in search_dic:
                    if word[index] == ".":
                        for i in search_dic["."]:
                            q.append((index+1, search_dic[i]))
                        continue
                    q.append((index+1, search_dic[word[index]]))
            
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)