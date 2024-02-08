class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prev_row = 0
        for row in bank:
            bit_set = row.count("1")
            result += prev_row * bit_set
            if bit_set != 0:
                prev_row = bit_set
        return result
