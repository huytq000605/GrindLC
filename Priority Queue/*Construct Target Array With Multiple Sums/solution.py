class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        total = 0
        for num in target:
            heappush(heap, -num)
            total += num
        # assume max_num is very big and v1, v2 is small
        # [max_num, v1, v2]
        # [max_num - (v1 + v2), v1, v2]
        # [max_num - 2 * (v1 + v2), v1, v2]
        # ...
        # [max_num - n * (v1 + v2), v1, v2]
        # => [max_num % (v1+v2), v1, v2]
        while True:
            max_value = -heappop(heap)
            total -= max_value
            if max_value == 1 or total == 1:
                return True
            if max_value <= total or total == 0 or max_value % total == 0 :
                return False
            max_value %= total
            total += max_value
            heappush(heap, -max_value)
            
        return True
            
            