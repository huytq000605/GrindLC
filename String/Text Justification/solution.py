class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current = []
        current_length = 0
        
        def push_to_result():
            nonlocal current, current_length, result
            spaces = maxWidth - current_length
            words = len(current)
            if words == 1:
                result.append(current[0] + " " * (maxWidth - len(current[0])) )
                return
            each_space = spaces // (words - 1)
            first_bonus = spaces % (words-1)
            s = ""
            for idx, word in enumerate(current):
                if idx > 0:
                    s += " " * (each_space)
                    if idx <= first_bonus:
                        s += " "
                s += word
            result.append(s)
            
        for word in words:
            total_length = current_length + len(current) - 1
            if len(current) == 0 or total_length + 1 + len(word) <= maxWidth:
                current.append(word)
                current_length += len(word)
            else:
                push_to_result()
                current = [word]
                current_length = len(word)
        last_s = ""
        for idx, word in enumerate(current):
            if idx > 0:
                last_s += " "
            last_s += word
        last_s += " " * (maxWidth - len(last_s))
        result.append(last_s)
            
        
        return result