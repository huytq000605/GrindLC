class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        n = len(nums)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        result = [-1 for i in range(n)]
        seen = dict()
        parents = set()
        
        # Memoize gcd
        @cache
        def gcd(num1, num2):
            if num2 > num2:
                num1, num2 = num2, num1
            if num2 == 0:
                return num1
            return gcd(num2, num1 % num2)
        
        # Inorder traversal
        def dfs(current, level):
            ans_level = -1
            # Since node's value is from 1 to 50, we can save value of them in previous and compare
            for num, (node, prev_level)  in seen.items():
                if gcd(nums[current], num) == 1:
                    # Found a closer node
                    if prev_level > ans_level:
                        ans_level = prev_level
                        result[current] = node
            # Original value before go to this node
            original = None
            if nums[current] in seen:
                original = [*seen[nums[current]]]

            # Add parent and change the seen value
            seen[nums[current]] = [current, level]
            parents.add(current)
            for next_node in tree[current]:
                if next_node in parents:
                    continue
                dfs(next_node, level + 1)
            # Revert back parents and seen value
            parents.remove(current)
            if original == None:
                seen.pop(nums[current])
            else:
                seen[nums[current]] = original
        dfs(0, 0)
        return result
