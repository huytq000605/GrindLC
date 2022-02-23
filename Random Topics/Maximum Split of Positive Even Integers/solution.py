class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        current = 2
        result = []
        while finalSum > 0:
            if finalSum < current:
                result.append(finalSum + result.pop())
                break
            result.append(current)
            finalSum -= current
            current += 2
        return result