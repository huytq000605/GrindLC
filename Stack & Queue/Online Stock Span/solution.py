class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1
        stack = self.stack
        while stack and stack[-1][0] <= price:
            result += stack.pop()[1]
        stack.append((price, result) )
        return result
    
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
