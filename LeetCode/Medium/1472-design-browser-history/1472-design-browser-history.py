class BrowserHistory:

    def __init__(self, homepage: str):
        self.page = [homepage]
        self.current = 0
        self.cnt = 1

    def visit(self, url: str) -> None:
        self.current += 1
        if self.current == len(self.page):
            self.page.append(url)
        else:
            self.page[self.current] = url
        self.cnt = self.current + 1

    def back(self, steps: int) -> str:
        self.current -= steps
        if self.current < 0:
            self.current = 0
        return self.page[self.current]

    def forward(self, steps: int) -> str:
        self.current += steps
        if self.current >= self.cnt:
            self.current = self.cnt - 1
        return self.page[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)