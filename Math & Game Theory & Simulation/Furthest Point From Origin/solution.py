class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        all_left = 0
        all_right = 0
        for m in moves:
            if m == "L":
                all_left -= 1
                all_right -= 1
            elif m == "R":
                all_left += 1
                all_right += 1
            else:
                all_left -= 1
                all_right += 1
        return max(abs(all_left), abs(all_right))
                
