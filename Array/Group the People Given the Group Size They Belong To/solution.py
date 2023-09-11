class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        groups = defaultdict(list)
        for i, group in enumerate(groupSizes):
            groups[group].append(i)
            if len(groups[group]) == group:
                result.append(groups[group])
                del groups[group]
        return result
