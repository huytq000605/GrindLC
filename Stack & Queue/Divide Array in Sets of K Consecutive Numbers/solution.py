class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        dq = deque()
        sets = 0
        prev_num = -1
        for num, freq in sorted(counter.items()):
            if sets > freq or (sets and num - 1 > prev_num): return False
            dq.append(freq - sets)
            sets = freq
            prev_num = num
            if len(dq) == k:
                sets -= dq.popleft()
        return sets == 0
