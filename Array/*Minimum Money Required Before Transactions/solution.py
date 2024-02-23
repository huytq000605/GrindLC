class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        result = 0
        max_cashback = 0
        max_cost = 0
        # Worst case is when we lose all money and then gain money
        # The worst case for losing money is when the max cashback is the last one
        # => Initial we need net_loss + max_cashback
        for cost, cashback in transactions:
            if cost >= cashback:
                result += (cost - cashback)
                max_cashback = max(max_cashback, cashback)
            else:
                max_cost = max(max_cost, cost)
        return result + max(max_cost, max_cashback)
