class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        result = 0
        for i in range(n):
            if colors[i] != colors[i-1] and colors[i] != colors[(i+1)%n]:
                result += 1
        return result
                
