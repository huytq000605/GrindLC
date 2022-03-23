class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        result = 0
        seen = set()
        MOD = 2 ** 31 - 1
        power = [pow(26, i, MOD) for i in range(len(text) // 2)]
        
        for length in range(1, len(text) // 2 + 1):
            left, right = 0, 0
            i, j = 0, length
            for k in range(length):
                left += (ord(text[i + k]) - ord('a') + 1) * power[k]
                left %= MOD
                
                right += (ord(text[j + k]) - ord('a') + 1) * power[k]
                right %= MOD
                
            if left == right:
                result += 1
                seen.add(text[i:j+length])
            i += 1
            j += 1
            while j + length - 1 < len(text):
                left -= (ord(text[i - 1]) - ord('a') + 1)
                left = (left + MOD) % MOD
                
                right -= (ord(text[j - 1]) - ord('a') + 1)
                right = (right + MOD) % MOD
                
                left //= 26
                right //= 26
                
                left += (ord(text[i + length - 1]) - ord('a') + 1) * power[length - 1]
                left %= MOD
                
                right += (ord(text[j + length - 1]) - ord('a') + 1) * power[length - 1]
                right %= MOD
                
                if left == right:
                    if text[i:j+length] not in seen:
                        seen.add(text[i:j+length])
                        result += 1

                i += 1
                j += 1
        return result