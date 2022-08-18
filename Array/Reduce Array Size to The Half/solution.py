class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        freq_count = Counter(counter.values())
        half = n // 2
        removed = 0
        result = 0
        freq = n
        while removed < half:
            while freq_count[freq] == 0: freq -= 1
            removed += freq
            result += 1
            freq_count[freq] -= 1
        return result
