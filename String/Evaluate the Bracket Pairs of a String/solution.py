class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        result = ""
        i = 0
        while i < len(s):
            if s[i] == "(":
                cur = ""
                while i + 1 < len(s) and s[i+1] != ")":
                    cur += s[i+1]
                    i += 1
                i += 1
                result += d.get(cur, "?")
            else:
                result += s[i]
            i += 1
        return result
