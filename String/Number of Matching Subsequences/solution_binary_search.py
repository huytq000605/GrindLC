class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        idxs = defaultdict(list)
        for i, c in enumerate(s):
            idxs[c].append(i)

        # Time complexity: 
        # len(s) + len(words) * max(len(word) for word in words) * log(len(s))
        def is_subseq(s):
            current = -1
            for c in s:
                if c in idxs:
                    start, end = 0, len(idxs[c]) - 1
                    while start < end:
                        mid = start + (end - start) // 2
                        if idxs[c][mid] <= current:
                            start = mid + 1
                        else:
                            end = mid
                    if idxs[c][start] <= current:
                        return False
                    current = idxs[c][start]
                else:
                    return False
            return True

        result = 0
        for word in words:
            if is_subseq(word):
                result += 1
        return result
