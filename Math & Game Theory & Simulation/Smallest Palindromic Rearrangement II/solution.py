class Solution:
    LIMIT = 10**6
    def smallestPalindrome(self, s: str, k: int) -> str:
        counter = [0 for _ in range(26)]
        offset = ord('a')
        for c in s:
            counter[ord(c) - offset] += 1
        mid = ""
        for c in range(26):
            if not counter[c]: continue
            if counter[c] & 1:
                mid = chr(c + offset)
            counter[c] >>= 1
        n = sum(counter)
        def get_ways(n):
            result = 1
            for c in range(26):
                if not counter[c]: continue
                w = math.comb(n, counter[c])
                if w > self.LIMIT: return self.LIMIT + 1
                result *= w
                if result > self.LIMIT: return self.LIMIT + 1
                n -= counter[c]
            return result
        if get_ways(n) < k: return ""
        
        result = ""
        for i in range(n):
            for c in range(26):
                if not counter[c]: continue
                ch = chr(c + offset)
                counter[c] -= 1
                ways = get_ways(n - i - 1)
                if ways >= k:
                    result += ch
                    break
                else:
                    counter[c] += 1
                    k -= ways
        return result + mid + result[::-1]
