class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        counter = Counter(basket1 + basket2)
        for freq in counter.values(): 
            if freq % 2: return -1
        
        n = len(basket1)
        result = 0
        mn = min(min(basket1), min(basket2))
        need = []
        
        c1, c2 = Counter(basket1), Counter(basket2)
        for price in counter.keys():
            if c1[price] != c2[price]:
                for _ in range(abs(counter[price] // 2 - c1[price])):
                    need.append(price)
        need.sort()
        for price in need[:len(need)//2]:
            result += min(price, mn*2)

        return result
            
