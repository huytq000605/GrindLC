class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        @cache
        def dfs(i):
            if i >= len(s): return [""]
            cur = ""
            result = []
            for idx in range(i, len(s)):
                cur += s[idx]
                if cur in words:
                    suffixes = dfs(idx + 1)
                    for suffix in suffixes:
                        result.append(cur + (" " if suffix != "" else "") + suffix)
            return result
        return dfs(0)
