class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        score = defaultdict(int)
        for idx, num in enumerate(nums[:-1]):
            if num == key:
                score[nums[idx + 1]] += 1
        max_score = 0
        result = 0
        for key, value in score.items():
            if value > max_score:
                max_score = value
                result = key
        return result