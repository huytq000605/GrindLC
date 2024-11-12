class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda item: item[0])
        maxBeauty = 0
        maxBeautyMap = {}
        result = [0] * len(queries)
        
        for price, beauty in items:
            maxBeauty = max(maxBeauty, beauty)
            maxBeautyMap[price] = maxBeauty
        prices = list(maxBeautyMap.keys())
        
        for idx, query in enumerate(queries):
            start = 0
            end = len(prices) - 1
            while start < end:
                mid = start + math.ceil((end - start + 1) / 2)
                if prices[mid] <= query:
                    start = mid
                else:
                    end = mid - 1
            if prices[start] > query:
                continue
            result[idx] = maxBeautyMap[prices[start]]
            
        return result
                    
