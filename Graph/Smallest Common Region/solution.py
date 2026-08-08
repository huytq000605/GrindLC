class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parents = {region[i]:region[0] for region in regions for i in range(1, len(region))}
        seen = set()
        while region1 in parents:
            seen.add(region1)
            region1 = parents[region1]
        while region2 in parents:
            if region2 in seen: return region2
            region2 = parents[region2]
        return region1
