class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(n)]
        robots.sort()
        
        result = [healths[i] for i in range(n)]
        
        lefts = []
        for p, h, d, i in robots:
            if d == "R":
                lefts.append((i, h))
            else:
                while lefts:
                    li, lh = lefts[-1]
                    if h < lh:
                        lefts[-1] = (li, lh-1)
                        result[li] -= 1
                        result[i] = -1
                        break
                    elif h > lh:
                        lefts.pop()
                        result[li] = -1
                        h -= 1
                        result[i] -= 1
                    else:
                        result[i] = -1
                        lefts.pop()
                        result[li] = -1
                        break
        
        new_result = []
        for r in result:
            if r == -1:
                continue
            new_result.append(r)
        return new_result
                        
            
