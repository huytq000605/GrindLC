class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        prev = -1
        # distance from i to the closest right on the left
        right = [n for i in range(n)]
        
        # distance from i to the closest left on the right
        left = [n for i in range(n)]
        
        for i in range(n):
            d = dominoes[i]
            if d == "R":
                prev = i
            elif d == "L":
                prev = -1
            
            if d == "." and prev != -1:
                right[i] = i - prev
                
        prev = -1
        for i in range(n-1, -1, -1):
            d = dominoes[i]
            if d == "L":
                prev = i
            elif d == "R":
                prev = -1
            
            if d == "." and prev != -1:
                left[i] = prev - i
        
        result = ""
        for i in range(n):
            if dominoes[i] != ".":
                result += dominoes[i]
            elif left[i] > right[i]:
                result += "R"
            elif left[i] < right[i]:
                result += "L"
            else:
                result += "."
        return result
            
