from heapq import heappush, heappop
from typing import List

class Solution:
    class HeapNode(list):
        def __lt__(self, other):
            if self[1] < other[1]:
                return True
            elif self[1] == other[1] and self[0] > other[0]:
                return True
            else:
                return False
            
        def __gt__(self, other):
            if self[1] > other[1]:
                return True
            elif self[1] == other[1] and self[0] < other[0]:
                return True
            else:
                return False

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = dict()
        min_heap = []
        my_list = []
        for word in words:
            if(freqs.get(word) == None): 
                freqs[word] = 0
            freqs[word] += 1
            
        for word, freq in freqs.items():
            my_list.append(self.HeapNode([word, freq]))
        
        
        for node in reversed(my_list):
            if len(min_heap) < k:
                heappush(min_heap, node)
            else:
                pop_node = heappop(min_heap)
                
                if node < pop_node:
                    heappush(min_heap, pop_node)
                else:
                    heappush(min_heap, node)
        result = []

        while len(min_heap) > 0:
            result.insert(0, heappop(min_heap)[0])
        return result
    
        
                