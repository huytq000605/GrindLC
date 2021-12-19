class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = ""
        idx = 0
        for i, l in enumerate(s):
            if idx < len(spaces) and i == spaces[idx]:
                result += " "
                idx += 1
            result += l
        
        return result