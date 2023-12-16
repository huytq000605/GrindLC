class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        prefix = [[0, 0]]
        for i, c in enumerate(s):
            cur = [*prefix[-1]]
            if c in "ueoai":
                cur[0] += 1
            else:
                cur[1] += 1
            prefix.append(cur)
        result = 0
        for start in range(len(s)):
            for end in range(start, len(s)):
                vowels = prefix[end+1][0] - prefix[start][0]
                consonants = prefix[end+1][1] - prefix[start][1]
                if vowels == consonants and (vowels * consonants) % k == 0:
                    result += 1
        return result
