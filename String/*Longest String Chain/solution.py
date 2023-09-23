class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            buckets[len(word)].append(word)
        result = 1
        dp = dict()
        
        def is_predecessor(w1, w2):
            i = 0
            for c in w2:
                if i == len(w1) or c != w1[i]:
                    continue
                i += 1
            return i == len(w1)
        
        for l in range(1, 16):
            if l not in buckets: continue
            if l + 1 not in buckets: continue
            for w1 in buckets[l]:
                for w2 in buckets[l+1]:
                    if is_predecessor(w1, w2):
                        dp[w2] = max(dp.get(w2, 1), dp.get(w1, 1) + 1)
                        result = max(dp[w2], result)
        return result
