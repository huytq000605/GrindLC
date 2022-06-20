class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = []
        for group in range(n):
            heappush(heap, (nums[group][0], group, 0))
        arr = []
        while heap:
            num, group, idx = heappop(heap)
            if idx + 1 < len(nums[group]):
                heappush(heap, (nums[group][idx+1], group, idx + 1))
            arr.append((num, group))
        result = [arr[0][0], arr[-1][0]]
        start = 0
        count = defaultdict(int)
        for num, group in arr:
            count[group] += 1
            while len(count) == n:
                if num - arr[start][0] < result[1] - result[0]:
                    result = [arr[start][0], num]
                count[arr[start][1]] -= 1
                if count[arr[start][1]] == 0:
                    count.pop(arr[start][1])
                start += 1
        return result