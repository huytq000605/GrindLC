class Solution:
    def intToRoman(self, num: int) -> str:
        convert = [
            ['M', 1000],
            ['CM', 900],
            ['D', 500],
            ['CD', 400],
            ['C', 100],
            ['XC', 90],
            ['L', 50],
            ['XL', 40],
            ['X', 10],
            ['IX', 9],
            ['V', 5],
            ['IV', 4],
            ['I', 1]
        ]
        
        idx = 0
        result = ""
        while(num > 0):
            while num < convert[idx][1]:
                idx += 1
            result += convert[idx][0]
            num -= convert[idx][1]
        return result