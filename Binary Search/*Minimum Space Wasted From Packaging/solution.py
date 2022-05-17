import math
from typing import *

class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        n = len(boxes)
        packages.sort()
        result = math.inf
        space_need = sum(packages)
        for supplier in range(n):
            boxes[supplier].sort()
            if boxes[supplier][-1] < packages[-1]:
                continue
            current_box = 0
            current_package = 0
            total_space = 0
            while current_package < len(packages):
                # can do binary_search here for more optimization
                if packages[current_package] > boxes[supplier][current_box]:
                    current_box += 1
                    continue
                
                start = current_package
                end = len(packages) - 1
                while start < end:
                    mid = start + math.ceil((end - start + 1) / 2)
                    if packages[mid] > boxes[supplier][current_box]:
                        end = mid - 1
                    else:
                        start = mid   
                total_space += (start - current_package + 1) * boxes[supplier][current_box]
                current_package = start + 1
                current_box += 1
            result = min(result, total_space - space_need)
        if result == math.inf:
            return -1
        return result % (10**9 + 7)