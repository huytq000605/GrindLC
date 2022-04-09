class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = defaultdict(list)
        max_freq = 0
        for num, freq in counter.items():
            buckets[freq].append(num)
            max_freq = max(max_freq, freq)

        result = []
        while max_freq > 0 and len(result) < k:
            if max_freq in buckets:
                for num in buckets[max_freq]:
                    result.append(num)
            max_freq -= 1
        return result
