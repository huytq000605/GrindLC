class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        # pref[i] = arr[0] ^ ... ^ arr[i-1] ^ arr[i]
        # pref[i-1] = arr[0] ^ ... ^ arr[i-1]
        # => arr[i] = pref[i] ^ pref[i-1]
        result = [pref[i] ^ pref[i-1] if i > 0 else pref[0] for i in range(0, n)]
        return result
