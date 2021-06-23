from typing import List, Tuple
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(maxsize = None)
        def shopping(needs: Tuple[int], current: int) -> int:
            result = current
            for idx, need in enumerate(needs):
                result += price[idx] * need
            
            for spec in special:
                isValidBuy = True
                for idx, need in enumerate(needs):
                    if spec[idx] > needs[idx]:
                        isValidBuy = False
                        break
                
                if isValidBuy:
                    needsAfterBuy = [0] * len(needs)
                    for index, need in enumerate(needsAfterBuy):
                        needsAfterBuy[index] = needs[index] - spec[index]
                    
                    res = shopping(tuple(needsAfterBuy), current + spec[-1])
                    result = min(result, res)
                
            return result
        return shopping(tuple(needs), 0)
                        
                        