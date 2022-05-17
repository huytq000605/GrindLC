class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
				# generate half the palindrome, if intLength is odd, get intLength // 2 + 1
        base = 10 ** ((intLength + 1) // 2 - 1)
        result = [-1 for i in range(len(queries))]
        for i, query in enumerate(queries):
            query = query - 1 + base
            s = str(query)
            if intLength % 2 == 0:
                palindrome = s + s[::-1]
            else:
                palindrome = s[:-1] + s[::-1]
            if len(palindrome) != intLength:
                continue
            result[i] = int(palindrome)
        return result