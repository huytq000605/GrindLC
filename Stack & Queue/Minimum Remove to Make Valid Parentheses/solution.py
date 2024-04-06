class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        close_remain = s.count(")")
        cur_open = 0
        result = ""
        for c in s:
            if c == "(":
                if(cur_open + 1 > close_remain): continue
                cur_open += 1
            elif c == ")":
                close_remain -= 1
                if(not cur_open): continue
                cur_open -= 1
            result += c
        return result
