class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = [[]]
        for num in nums:
            if len(result[-1]) == 3:
                result.append([])
            for prev in result[-1]:
                if prev + k < num:
                    return []
            result[-1].append(num)
        return result
            
            
