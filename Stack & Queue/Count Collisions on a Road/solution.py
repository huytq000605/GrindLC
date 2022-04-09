class Solution:
    def countCollisions(self, directions: str) -> int:
        last = "L"
        num = 0
        result = 0
        for d in directions:
            if d == "L":
                if last == "S":
                    result += 1
                elif last == "R":
                    result += num
                    result += 1
                    num = 0
                    last = "S"
            elif d == "R":
                last = "R"
                num += 1
            else:
                if last == "R":
                    result += num
                    num = 0
                last = "S"
        return result