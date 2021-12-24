import math
import collections

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = math.inf
        lookup = collections.defaultdict(list)
        n = len(arr)
        for i in range(n-1):
          diff = arr[i+1] - arr[i]
          min_diff = min(min_diff, diff)
          lookup[diff].append([arr[i], arr[i+1]])
        return lookup[min_diff]