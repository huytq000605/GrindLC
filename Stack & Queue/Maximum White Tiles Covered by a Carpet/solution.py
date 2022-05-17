class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpet: int) -> int:
        tiles.sort()
        result = 0
        arr = deque()
        cur = 0
        for s, e in tiles:
            if e - s + 1 >= carpet:
                return carpet
            else:
                remain = carpet - (e-s+1)
                start_carpet = s - remain
                while arr and arr[0][0] < start_carpet:
                    if arr[0][1] < start_carpet:
                        first = arr.popleft()
                        cur -= (first[1] - first[0] + 1)
                    else:
                        cur -= (start_carpet - arr[0][0])
                        arr[0][0] = start_carpet
                cur += (e-s+1)
                arr.append([s, e])
                result = max(result, cur)
        return result