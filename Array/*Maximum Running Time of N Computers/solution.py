class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        heap = [-b for b in batteries]
        heapq.heapify(heap)
        s = sum(batteries)
        # we want to split sum(batteries) evenly into n computers
        # we may not achieve that only if theres battery B > sum(batteries) // n
        # if that happens, we plug battery B to that computer forever
        # solve the problem with n-1 computers and without battery B

        # Example:
        # Sort the batteries by their engry from high to low, then assign the first N batteries (with the most energy) to the N computers, and let's call these N batteries "main" batteries. All the other non-empty batteries will be called "extra" batteries.
        # At the beginning of each minute, assuming now we still have M non-empty "extra" batteries, use them to charge computers in replacement of the M "main" batteries with currently lowest energy. Then run all the computers for 1 minute.
        # Repeat step 2 until at least one "main" battery is exhausted, while all "extra" batteries should have already been exhausted too (no later than any "main" battery). This is because all "extra" battery are always being used before they are exhausted, and they all have an initial energy level less than or equal to the lowest one of those "main" batteries.
        # The number of minutes passed in this way is the final answer.
        while n > 1 and -heap[0] > s // n:
            n -= 1
            s += heapq.heappop(heap)
        return s // n
