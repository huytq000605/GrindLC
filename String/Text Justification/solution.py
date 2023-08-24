class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start = 0
        i = 0
        length = 0
        while i < len(words):
            word = words[i]
            # first word
            if not length:
                length = len(word)
                i += 1
            # if still can append
            elif length + len(word) + (i - start) <= maxWidth:
                length += len(word)
                i += 1
            # cannot append words[i], append new line
            else:
                number_of_words = i - start
                spaces = maxWidth - length
                line = ""
                if number_of_words == 1:
                    line = words[start] + " " * (maxWidth - len(words[start]))
                else:
                    each = spaces // (number_of_words-1)
                    remaining = spaces - each * (number_of_words-1)
                    for idx in range(start, i):
                        if idx != start:
                            line += " " * each
                            if remaining: 
                                line += " "
                                remaining -= 1
                        line += words[idx]

                # append line
                result.append(line)
                # assign start and reset length
                start = i
                length = 0
        # last line
        line = ""
        for idx in range(start, len(words)):
            if idx != start:
                line += " "
            line += words[idx]
        line += " " * (maxWidth - len(line))
        result.append(line)
        return result
            
