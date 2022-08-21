class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp, target = list(stamp), list(target)
        t, s = len(target), len(stamp)
        result = []
        def reverse(start):
            changed = False
            for i in range(s):
                if target[i + start] == "?": continue
                if stamp[i] != target[i + start]: return False
                changed = True
            if changed:
                target[start:start+s] = ['?' for i in range(start, start + s)]
                result.append(start)
            return changed
        
        changed = True
        while changed:
            changed = False
            for i in range(t - s + 1):
                changed |= reverse(i)

        if False in [letter == "?" for letter in target]:
            return []
        return reversed(result)
        
