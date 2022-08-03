class TreeNode():
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None

class MyCalendar:

    def __init__(self):
        self.bst = None

    def book(self, start: int, end: int) -> bool:
        node = TreeNode(start, end)
        if not self.bst:
            self.bst = node
            return True
        parent = None
        current = self.bst
        while True:
            if not current:
                if start >= parent.end:
                    parent.right = node
                else:
                    parent.left = node
                return True
            parent = current
            if start >= current.end:
                current = current.right
                continue
            elif end <= current.start:
                current = current.left
                continue
            return False
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
