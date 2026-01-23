
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        prev = [i-1 for i in range(n)]
        nxt = [i+1 for i in range(n)]
        pq = []
        desc = 0
        for i in range(n-1):
            heappush(pq, (nums[i] + nums[i+1], i))
            if nums[i] > nums[i+1]: desc += 1
        result = 0
        while desc:
            s, i = heappop(pq)
            j = nxt[i]
            if j >= n or prev[j] != i or s != nums[i] + nums[j]:
                continue
            result += 1
            p, q = prev[i], nxt[j]
            if nums[i] > nums[j]:
                desc -= 1
            if p != -1 and nums[p] > nums[i]:
                desc -= 1
            if q != n and nums[j] > nums[q]:
                desc -= 1
            nxt[i] = q
            prev[j] = -1
            if q != n: prev[q] = i
            nxt[j] = n
            nums[i] = s
            if p != -1:
                heappush(pq, (nums[p] + s, p))
                if nums[p] > nums[i]: desc += 1
            if q != n:
                heappush(pq, (s + nums[q], i))
                if nums[i] > nums[q]: desc += 1
        
        return result

