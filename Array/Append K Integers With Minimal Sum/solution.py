class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = [0, *sorted(nums)]
        result = 0
        
        for i in range(len(nums)-1):
            if k == 0:
                break
            num = nums[i]
            next_num = nums[i + 1]
            if next_num - num <= 1:
                continue
            
            no = min(k, next_num - num - 1)
            last_num = num + no
            result += (last_num + (num + 1)) * no // 2
            k -= no
        
        if k > 0:
            last_num = nums[-1] + k
            result += (last_num + (nums[-1] + 1)) * k // 2
        return result