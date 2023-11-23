class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        for i in range(len(l)):
            left, right = l[i], r[i]
            mn, mx = min(nums[left:right+1]), max(nums[left:right+1])

            if (mx - mn) % (right - left) != 0:
                result.append(False)
                continue

            d = (mx - mn) // (right - left)
            if d == 0:
                result.append(True)
                continue
            
            have = set()
            for idx in range(left, right + 1):
                have.add(nums[idx])

            valid = True
            for num in range(mn, mx+1, d):
                if num not in have:
                    valid = False
                    print(num)
                    break
            result.append(valid)
        return result    
        
