class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 0
        result = []
        for num in range(1, n+1):
            result.append("Push")
            if num != target[i]:
                result.append("Pop")
            else:
                i += 1
            if i == len(target):
                return result
        return result
