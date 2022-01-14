class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        no_of_balls = 0
        result = 0
        inventory.sort(reverse = True)
        inventory.append(0)
        for idx in range(len(inventory) - 1):
            no_of_balls += 1
            price = inventory[idx]
            next_price = inventory[idx + 1]
            if next_price == price:
                continue
            times = price - next_price

            if no_of_balls * times >= orders:
                times = orders // no_of_balls
                result += (((price + (price - times + 1)) * (times)) // 2) * no_of_balls
                orders = orders % no_of_balls
                result += (price - times) * orders
                return result % (10 ** 9 + 7)
            else:
                result += (((price + (price - times + 1)) * (times)) // 2) * no_of_balls
                orders -= no_of_balls * times
        # Never goes here
        return result % (10 ** 9 + 7)
