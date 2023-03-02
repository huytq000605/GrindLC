class Solution:
    def compress(self, chars: List[str]) -> int:
        letter, freq = "", 0
        i = 0
        def update():
            nonlocal i, letter, freq
            chars[i] = letter
            i += 1
            if freq > 1:
                for f in str(freq):
                    chars[i] = f
                    i += 1
            freq = 0
            
        for c in chars:
            if c != letter and freq > 0:
                update()       
            letter = c
            freq += 1
        update()
        return i
