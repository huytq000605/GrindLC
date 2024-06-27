class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        result = []
        for num in arr2:
            counter[num] -= 1
            for _ in range(counter[num] + 1):
                result.append(num)
            del counter[num]
        for num, freq in sorted(counter.items(), key = lambda e: e[0]):
            for _ in range(freq): result.append(num)
        return result
