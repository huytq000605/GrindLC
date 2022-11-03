class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        seen = set([start])
        q = deque([(start, 0)])
        while q:
            gen, s = q.popleft()
            for i in range(8):
                for replace in "ACGT":
                    target = gen[:i] + replace + gen[i+1:]
                    if target in bank and target not in seen:
                        if target == end:
                            return s+1
                        seen.add(target)
                        q.append((target, s+1))
        return -1
                
            
