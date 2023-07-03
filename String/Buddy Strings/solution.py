class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        diffs = []
        same = False
        set_s = set()
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append((s[i], goal[i]))
            if s[i] in set_s:
                same = True
            set_s.add(s[i])
        if not diffs and same: return True
        if len(diffs) != 2 or diffs[0][1] != diffs[1][0] or diffs[0][0] != diffs[1][1]:
            return False
        return True
