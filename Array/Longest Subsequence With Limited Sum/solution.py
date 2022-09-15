class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        for query in queries:
            total = 0
            length = 0
            for num in nums:
                if total + num > query:
                    break
                total += num
                length += 1
            result.append(length)
        return result
