class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.DIR = [[1, 0, "East"], [0, 1, "North"], [-1, 0, "West"], [0, -1, "South"]]
        self.idx = 0

    def move(self, num: int) -> None:
        DIR = self.DIR
        idx = self.idx
        while num > 0:
            move = 0
            if DIR[idx][0] > 0:
                move = min(num, self.width - 1 - self.x)
            elif DIR[idx][0] < 0:
                move = min(num, self.x)
            elif DIR[idx][1] > 0:
                move = min(num, self.height - 1 - self.y)
            else:
                move = min(num, self.y)
            if move == 0:
                mod = self.width * 2 + self.height * 2 - 4
                if num >= mod:
                    num %= mod
                    continue
                idx = (idx + 1) % 4
            self.x += DIR[idx][0] * move
            self.y += DIR[idx][1] * move
            num -= move
        self.idx = idx
            
                

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.DIR[self.idx][2]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.move(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()