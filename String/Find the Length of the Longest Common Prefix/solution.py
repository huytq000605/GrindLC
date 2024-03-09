class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixs = set()
        for num in arr1:
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixs.add(s[:i])
        
        result = 0
        for num in arr2:
            s = str(num)
            for i in range(len(s), 0, -1):
                if s[:i] in prefixs:
                    result = max(result, i)
                    break
        return result
