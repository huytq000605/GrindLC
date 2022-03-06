class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        r = s.split(":")
        result = []
        for row in range(ord(r[0][0]) - ord('a'), ord(r[1][0]) - ord('a') + 1):
            for col in range(int(r[0][1]), int(r[1][1]) + 1):
                a = chr(row+ord('a'))
                b = str(col)
                result.append(a+b)
        return result