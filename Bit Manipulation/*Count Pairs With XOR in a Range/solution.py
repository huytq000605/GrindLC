class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = {}
        result = 0
        
        def insert_to_trie(num):
            current = trie
            for i in range(15, -1, -1):
                next_node = (num >> i) & 1
                if next_node not in current:
                    current[next_node] = {'count': 1}
                else:
                    current[next_node]['count'] += 1
                current = current[next_node]
        
        def count_less_than_or_equal(xor_with, limit):
            current = trie
            result = 0
            for i in range(15, -1, -1):
                bit_limit = (limit >> i) & 1
                bit_xor = (xor_with >> i) & 1
                if bit_limit == 1:
                    if bit_xor in current:
                        result += current[bit_xor]['count']
                    if 1 - bit_xor not in current:
                        current = None
                        break
                    current = current[1 - bit_xor]
                else:
                    if bit_xor not in current:
                        current = None
                        break
                    current = current[bit_xor]
            if current:
                result += current['count']
            return result        
        
        for num in nums:
            result += count_less_than_or_equal(num, high) - count_less_than_or_equal(num, low-1)
            
            insert_to_trie(num)

        return result