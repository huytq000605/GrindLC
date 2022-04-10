class Solution:
    def maximumBeauty(self, flowers: List[int], new: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers = [min(target, flowers[i]) for i in range(n)]
        total = sum(flowers)
        if total == target * n:
            return full * n
        
        if total + new >= target * n:
            return max(full * n, full * (n-1) + (target - 1) * partial)
        
        flowers.sort()
        prefix = [0 for i in range(n)]
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i-1]
            prefix[i] += flowers[i]
        result = 0
        j = n - 1
        while j >= 0:
            if flowers[j] == target:
                j -= 1
                continue
            start = flowers[0]
            end = target - 1
            while start < end:
                mid = start + math.ceil((end - start + 1) / 2)
                
                # highest idx that flowers[i] <= mid with i in [0, j]
                
                # left = 0
                # right = j
                # while left < right:
                #     idx = left + math.ceil((right - left + 1) / 2)
                #     if flowers[idx] > mid:
                #         right = idx - 1
                #     else:
                #         left = idx
                # idx = left
                
                idx = bisect_right(flowers, mid, lo = 0, hi = j)
                if flowers[idx] > mid:
                    idx -= 1

                if mid * (idx + 1) - prefix[idx] > new:
                    end = mid - 1
                else:
                    start = mid
            
            min_value = start
            result = max(result, min_value * partial + full * (n - j - 1))
            if target - flowers[j] > new:
                break
            new -= target - flowers[j]
            j -= 1
        return result