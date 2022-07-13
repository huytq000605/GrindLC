class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        s1, s2 = "", ""
        for i in range(n):
            if start[i] != "_":
                s1 += start[i]
            if target[i] != "_":
                s2 += target[i]
        if s1 != s2:
            return False

        target_r = 0
        cur_r = 0
        for i in range(n):
            if start[i] == "R":
                cur_r += 1
            if target[i] == "R":
                target_r += 1
            if target_r > cur_r:
                return False

        target_l = 0
        cur_l = 0
        for i in range(n-1, -1, -1):
            if start[i] == "L":
                cur_l += 1
            if target[i] == "L":
                target_l += 1
            if target_l > cur_l:
                return False
        return True
