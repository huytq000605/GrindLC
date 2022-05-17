class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        start, end = 0, max(arr)
        result_diff = math.inf
        result = math.inf
        while start <= end:
            total = 0
            choose = start + (end - start) // 2
            for num in arr:
                if num <= choose:
                    total += num
                else:
                    total += choose
            if total == target:
                return choose
            elif total < target:
                start = choose + 1
            else:
                end = choose - 1
            diff = abs(target - total)
            if diff == result_diff:
                result = min(result, choose)
            elif diff < result_diff:
                result_diff = diff
                result = choose
        return result
            
