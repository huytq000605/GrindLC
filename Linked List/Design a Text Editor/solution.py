class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class TextEditor:

    def __init__(self):
        self.cursor = Node("") 

    def addText(self, text: str) -> None:
        for c in text:
            node = Node(c)
            cur_next = self.cursor.next
            self.cursor.next = node
            node.prev = self.cursor
            if cur_next:
                cur_next.prev = node
                node.next = cur_next
            self.cursor = node

    def deleteText(self, k: int) -> int:
        result = 0
        while self.cursor.val != "" and k:
            current_cursor = self.cursor
            current_next = self.cursor.next
            self.cursor = current_cursor.prev
            self.cursor.next = current_cursor.next
            if current_next:
                current_next.prev = self.cursor
            result += 1
            k -= 1
        return result
        

    def cursorLeft(self, k: int) -> str:
        while k and self.cursor.val != "":
            self.cursor = self.cursor.prev
            k -= 1
        return self.get_text()
        
    
    def get_text(self):
        result = ""
        k = 10
        current = self.cursor
        while k and current.val != "":
            result += current.val
            current = current.prev
            k -= 1
        return result[::-1]

    def cursorRight(self, k: int) -> str:
        while k and self.cursor.next:
            self.cursor = self.cursor.next
            k -= 1
        return self.get_text()


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)