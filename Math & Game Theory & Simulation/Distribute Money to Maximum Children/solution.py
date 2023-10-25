class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children: return -1
        if money == 4 and children == 1: return -1
        valid = 0
        money -= children
        while money > 7 and valid < children - 1:
            money -= 7
            valid += 1
        if money == 3 and children - valid == 1: valid -= 1
        if money == 7: valid += 1
        return valid
            
