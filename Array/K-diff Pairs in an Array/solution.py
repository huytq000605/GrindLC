class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0
        for num in counter.keys():
            if k != 0:
                if num + k in counter:
                    result += 1
                if num - k in counter:
                    result += 1
            else:
                if counter[num] > 1:
                    result += 2
        return result // 2