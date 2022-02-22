class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(len(queries)):
            queries[i].append(i)
        nums = sorted(set(nums))
        queries.sort(key = lambda query: query[1])
        idx = 0
        trie = {}
        result = [-1 for i in range(len(queries))]
        for x, m, original_index in queries:
            while idx < len(nums) and nums[idx] <= m:
                current = trie
                for i in range(31, -1, -1):
                    key = (nums[idx] >> i) & 1
                    if key not in current:
                        current[key] = {}
                    current = current[key]
                idx += 1
            
            current = trie
            xor_with = 0
            no_answer = False
            for i in range(31, -1, -1):
                key = 1 - ((x >> i) & 1)
                if key not in current:
                    key = 1 - key
                    if key not in current:
                        no_answer = True
                        break
                current = current[key]
                xor_with |= key << i
            if no_answer:
                continue
            result[original_index] = xor_with ^ x
        return result