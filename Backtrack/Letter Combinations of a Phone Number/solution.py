class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        current_level = [""]
        for digit in digits:
            next_level = []
            for current in current_level:
                for letter in letters[digit]:
                    next_level.append(current + letter)
            current_level = next_level
        return current_level