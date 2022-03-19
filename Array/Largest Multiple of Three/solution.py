class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        freq = Counter(digits)
        total = sum(digits)
        
        def build():
            result = ""
            for i in range(9, -1, -1):
                if result == "" and i == 0 and freq[i] > 0:
                    return "0"
                result += str(i) * freq[i]
            return result
        
        if total % 3 == 0:
            return build()
        
        if total % 3 == 1:
            for i in [1,4,7]:
                if freq[i] > 0:
                    freq[i] -= 1
                    return build()
            
            count = 2
            while count > 0:
                for i in [2,5,8]:
                    while count > 0 and freq[i] > 0:
                        freq[i] -= 1
                        count -= 1
            return build()
        
        if total % 3 == 2:
            for i in [2,5,8]:
                if freq[i] > 0:
                    freq[i] -= 1
                    return build()
            
            count = 2
            while count > 0:
                for i in [1,4,7]:
                    while count > 0 and freq[i] > 0:
                        freq[i] -= 1
                        count -= 1
            return build()