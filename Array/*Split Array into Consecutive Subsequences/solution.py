class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        # Count how many num do we have
        counter = Counter(nums)
        # How many subsequences end at num
        end = Counter()
        for num in nums:
            if counter[num] == 0: continue
            counter[num] -= 1
            # Extend found subsequences
            if end[num-1] > 0:
                end[num-1] -= 1
                end[num] += 1
            # If cannot extend any, create new subsequences
            elif counter[num+1] > 0 and counter[num+2] > 0:
                end[num+2] += 1
                counter[num+1] -= 1
                counter[num+2] -= 1
            # Cannot make it
            else:
                return False
        return True
