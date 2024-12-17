class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = [0] * 26
        for letter in s:
            counter[ord(letter) - ord('a')] += 1
        i = 25
        result = ""
        current_letter = -1
        count = 0
        
        while i >= 0:
            while i >= 0 and counter[i] == 0:
                i -= 1
            if i < 0 == 0:
                break
            if current_letter == i and count == repeatLimit:
                j = i - 1
                while j >= 0 and counter[j] == 0:
                    j -= 1
                if j < 0:
                    break
                result += chr(j + ord('a'))
                counter[j] -= 1
                current_letter = j
                count = 1
            else:
                result += chr(i + ord('a'))
                if i == current_letter:
                    count += 1
                else:
                    count = 1
                    current_letter = i
                counter[i] -= 1
        return result