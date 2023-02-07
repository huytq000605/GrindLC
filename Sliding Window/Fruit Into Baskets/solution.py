class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        baskets = defaultdict(int)
        result = 0
        for i, fruit in enumerate(fruits):
            baskets[fruit] += 1
            while len(baskets) > 2:
                baskets[fruits[start]] -= 1
                if baskets[fruits[start]] == 0:
                    baskets.pop(fruits[start])
                start += 1
            result = max(result, i - start + 1)
        return result
