class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = False
        heavy = False
        if length >= 10**4 or width >= 10**4 or height >= 10**4 or length * width * height >= 10**9:
            bulky = True
        if mass >= 100:
            heavy = True
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"
