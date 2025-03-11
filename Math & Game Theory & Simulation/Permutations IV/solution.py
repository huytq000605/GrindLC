facts = [1 for _ in range(51)]
for i in range(2, 51):
    facts[i] = facts[i-1] * i
    
class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        odds = [i for i in range(1, n+1, 2)]
        evens = [i for i in range(2, n+1, 2)]
        result = []
        if len(odds) == len(evens):
            o, e = len(odds), len(evens)
            i = 0
            m = facts[o-1] * facts[e];
            while k > m and i < e+o-1:
                k -= m;
                i += 1
            if(k > m): return []
            if(i & 1):
                result.append(evens.pop(i//2));
            else:
                result.append(odds.pop(i//2));
        
        while evens or odds:
            o, e = len(odds), len(evens)
            i = 0
            if(o > e or (result[-1] & 1) == 0):
                m = facts[o-1] * facts[e];
                while(k > m and i < o-1):
                    k -= m;
                    i += 1
                if(k > m): return []
                result.append(odds.pop(i));
                
            else:
                m = facts[o] * facts[e-1];
                while(k > m and i < e-1):
                    k -= m;
                    i += 1
                
                if(k > m): return []
                result.append(evens.pop(i));
        return result;
