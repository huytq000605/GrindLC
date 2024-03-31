class Solution:
    def minOperations(self, k: int) -> int:
        # a increase
        # b copies
        # find min(a+b) for (a + 1) * (b + 1) >= k
        # => (a = b) or (b = a + 1)
        # => c * c >= k with c = a + 1
        # find c by math.ceil(math.sqrt(k)) due to >= k
        sqrt = math.ceil(math.sqrt(k))
        return (sqrt - 1) + math.ceil(k/sqrt) - 1
