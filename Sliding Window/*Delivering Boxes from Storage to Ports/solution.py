class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, max_box: int, max_weight: int) -> int:
        # We want to greedily take as many boxes as possible
        # But there are some cases like [a, w1], [b, w2], [c, w3], [c, w4], [c, w5], [c, w6]
        # Example like we can take w1, w2, w3, w4 together
        # But the best is when we take w1, w2 and w3 w4 w5 w6 together
        # So we use Sliding Window to cut down these last same port boxes for each position
        n = len(boxes)
        # dp[i] is min number of trip to deliver first i boxes
        dp = [0] + [math.inf for i in range(n)]
        j = 0
        last_j = 0
        weight = 0
        trips = 0
        
        for i in range(n):
            while j < n and j - i < max_box and weight + boxes[j][1] <= max_weight:
                weight += boxes[j][1]
                if j == 0 or boxes[j][0] != boxes[j-1][0]:
                    last_j = j
                    trips += 1
                j += 1
            # dp[j] takes boxes[0] to boxes[j-1], +1 for comeback to storage
            dp[j] = min(dp[j], dp[i] + trips + 1)
            # dp[last_j] so we dont take boxes[last_j] to boxes[j] => Save 1 trip
            dp[last_j] = min(dp[last_j], dp[i] + trips)
            
            weight -= boxes[i][1]
            if i == n - 1 or boxes[i][0] != boxes[i+1][0]:
                trips -= 1
        
        return dp[-1]