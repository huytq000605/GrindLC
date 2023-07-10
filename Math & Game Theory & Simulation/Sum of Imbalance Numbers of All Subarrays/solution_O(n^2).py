class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            s = set([nums[i]])
            cur = 0
            for num in nums[i+1:]:
                if num in s:
                    pass
                elif num-1 in s and num+1 in s:
                    cur -= 1
                elif num-1 not in s and num+1 not in s:
                    cur += 1
                s.add(num)
                result += cur
        return result
                    
                

            
                        
