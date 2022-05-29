class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        for i, d in enumerate(num):
            if counter[str(i)] != int(d):
                return False
        return True