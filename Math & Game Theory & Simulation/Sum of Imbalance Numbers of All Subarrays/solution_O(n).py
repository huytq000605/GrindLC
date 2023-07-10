class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        # left[i] = nearest idx where nums[idx] = nums[i] or nums[idx] = nums[i] + 1
        # nums[idx] = nums[i] because we don't want to count duplicated subarrays.
        left = [-1 for _ in range(n)]
        seen = defaultdict(lambda: -1)

        for i in range(n):
            left[i] = max(seen[nums[i]], seen[nums[i] + 1])
            seen[nums[i]] = i
        
        seen = defaultdict(lambda: n)
        # considering how many each number are contributing to the result
        for i in range(n-1, -1, -1):
            result += (i - left[i]) * (seen[nums[i] + 1] - i)
            seen[nums[i]] = i

        # we are counting the cases where nums[i] can be the maximum number in the subarray
        # number of that cases would be equal to the number of subarray
        result -= n*(n+1)//2
        return result

                

            
                        
