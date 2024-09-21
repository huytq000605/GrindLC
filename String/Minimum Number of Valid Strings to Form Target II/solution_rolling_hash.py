pw = random.randint(100, 200)
mod = random.getrandbits(40)

pws = [1]
for _ in range(10 ** 5):
    pws.append(pws[-1] * pw % mod)

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        
        vis = set()
        for w in words:
            x = 0
            for c in w:
                x = (x * pw + ord(c)) % mod
                vis.add(x)
        
        acc = [0]
        for c in target:
            acc.append((acc[-1] * pw + ord(c)) % mod)
        
        l = r = 0
        cnt = 0
        while r < n:
            nr = r
            for i in range(l, r + 1):
                left, right = i, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if (acc[mid+1] - acc[i] * pws[mid+1-i] % mod) % mod in vis:
                        left = mid + 1
                    else:
                        right = mid - 1
                if right + 1 > nr:
                    nr = right + 1
                mid = right
            if nr == r: return -1
            l, r = r + 1, nr
            cnt += 1
        return cnt
        
