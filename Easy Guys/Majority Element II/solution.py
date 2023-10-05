class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for num, c in counter.items():
            if c > len(nums) // 3:
                result.append(num)
        return result
            
