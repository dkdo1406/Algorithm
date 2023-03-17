class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node:
                node[i] = dict()
            node = node[i]
        node["*"] = ""

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node:
                return False
            node = node[i]
        
        return "*" in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node:
                return False
            node = node[i]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)