class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        buckets = defaultdict(list)
        for word in words:
            buckets[len(word)].append(word)
        result = 0
        longest_end_at = dict()
        for l in sorted(buckets.keys()):
            for word in buckets[l]:
                longest_end_at[word] = max([longest_end_at.get(word[:i] + word[i+1:], 0) + 1 for i in range(l)])
                result = max(result, longest_end_at[word])
        return result

