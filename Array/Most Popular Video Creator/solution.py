class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = defaultdict(list)
        total_views = defaultdict(int)
        n = len(ids)
        for i in range(n):
            c, i, v = creators[i], ids[i], views[i]
            total_views[c] += v
            d[c].append((-v, i))
        
        most_popular = max(total_views.values())
        result = []
        for c in total_views.keys():
            if total_views[c] == most_popular:
                d[c].sort()
                result.append((c, d[c][0][1]))
        return result
        
