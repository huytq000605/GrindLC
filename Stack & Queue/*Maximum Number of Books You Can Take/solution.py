class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        def ssum(num, size):
            size = min(size, num)
            return (num + (num - size + 1)) * size // 2
        result = 0
        cur = 0
        stack = []
        n = len(books)
        for i in range(n):
            while stack and books[stack[-1]] + (i - stack[-1]) >= books[i]:
                j = stack.pop()
                if stack:
                    cur -= ssum(books[j], j - stack[-1])
                else:
                    cur -= ssum(books[j], j + 1)
            # all the books `k` are not in the stack already satisfied
            # books[k] + (i - k) >= books[i]
            # so surely we can take books[i] - (i - k) books from books[k].
            if stack:
                cur += ssum(books[i], i - stack[-1])
            else:
                cur += ssum(books[i], i+1)
            stack.append(i)
            result = max(result, cur)
        return result
