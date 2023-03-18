class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = 0
        self.bound = 0
        self.history = [homepage]
    

    def visit(self, url: str) -> None:
        if len(self.history) == self.cur + 1:
            self.history.append(url)
        else:
            self.history[self.cur + 1] = url
        self.cur += 1
        self.bound = self.cur

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur - steps)
        return self.history[self.cur]
    
    def forward(self, steps: int) -> str:
        self.cur = min(self.bound, self.cur + steps)
        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
