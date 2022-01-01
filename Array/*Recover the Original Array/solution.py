class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        lookup = set(nums)
        # Since num is sorted, minimum must be original_arr[0] - k
        # Try find k and see
        for num in nums:
            k = (num - nums[0])
            if k % 2 == 1 or k == 0:
                continue
            k //= 2
            clear = defaultdict(int)
            result = []
            valid = True
            for num in nums:
                if num in clear and clear[num] > 0:
                    clear[num] -= 1
                    continue
                if (num + 2 * k) not in lookup:
                    valid = False
                    break
                result.append(num + k)
                if len(result) > len(nums) // 2:
                    valid = False
                    break
                clear[num + 2 * k] += 1
            if valid and len(result) == len(nums) // 2:
                return result
