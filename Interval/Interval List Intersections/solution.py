class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            if max(s1, s2) <= min(e1, e2):
                result.append([max(s1, s2), min(e1, e2)])
            if e1 >= e2: j += 1
            else: i += 1
        return result
