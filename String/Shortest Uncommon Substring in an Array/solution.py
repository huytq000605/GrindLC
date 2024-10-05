class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        substrings = Counter()
        for word in arr:
            m = len(word)
            for i in range(m):
                for j in range(i, m):
                    substrings[word[i:j+1]] += 1
        result = []
        for i, word in enumerate(arr):
            m = len(word)
            res = ""
            this_substrings = Counter()
            for j in range(m):
                for k in range(j, m):
                    this_substrings[word[j:k+1]] += 1
            for j in range(m):
                for k in range(j, m):
                    if res and len(res) < k - j + 1: break
                    ss = word[j:k+1]
                    if substrings[ss] - this_substrings[ss] == 0:
                        if not res or\
                            (k-j+1 < len(res)) or\
                            (k-j+1 == len(res) and ss < res):
                            res = ss
                            break
            result.append(res)
        return result 
            
