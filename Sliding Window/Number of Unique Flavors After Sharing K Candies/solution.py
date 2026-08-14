class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counter = Counter(candies)
        result = 0
        for i in range(len(candies)):
            if i >= k: counter[candies[i-k]] += 1
            counter[candies[i]] -= 1
            if not counter[candies[i]]: del counter[candies[i]]
            if i >= k-1: result = max(result, len(counter))
        return result
