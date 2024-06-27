class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # x would not send a friend request if
        # age[y] <= 0.5 * age[x] + 7
        # => 2 * (age[y] - 7) <= age[x]
        # // if age[y] == age[x] => age[x] - 14 <= 0 => age[x] <= 14
        # age[x] < age[y]
        ages.sort()
        result = 0
        x, y = 0, 0
        counter = Counter(ages)
        # handle special cases of equal ages
        # if ages > 14, they will send friend request to each other
        # but we need to exclude the duplicated case when we calculate in sliding window
        # 1st age sends to 0 ages before it
        # 2nd age sends to 1 age before it
        # 3rd age sends to 2 ages before it
        # ... kth age sends to k-1 ages before it
        # => k * (k-1) // 2
        for k, v in counter.items():
            if k > 14:
                result += (v-1) * v - v*(v-1)//2
        # sliding window
        while x < len(ages):
            while  y < len(ages) and 2 * (ages[y] - 7) <= ages[x]:
                y += 1
            result += x - min(y, x)
            x += 1
        return result

