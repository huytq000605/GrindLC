class Solution:
    def minimumBoxes(self, n: int) -> int:
        total = 0
        bottom = 0
        height = 0
				# Build perfect pyramid
        '''
        (1) (2) (4) (7)
        (3) (5) (8)
        (6) (9)
        (10)
        '''
        while total < n:
            height += 1
            bottom += height
            # Each height can build (height - 1) more stone
            total += bottom

        if total == n:
            return bottom
        # Delete last height pyramid
        total -= bottom
        bottom -= height
        height -= 1
        
				# Try to add one by one stone to build pyramid
				# Can use binary search with min = 0, max = height + 1
				# plus_bottom = k * (k+1) // 2
        plus_bottom = 0
        while total < n:
            plus_bottom += 1
            total += plus_bottom
        return bottom + plus_bottom