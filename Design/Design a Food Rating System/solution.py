class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.pqs = defaultdict(list)
        self.ratings = dict()
        self.food_to_cuisine = dict()
        n = len(foods)
        for i in range(n):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            heappush(self.pqs[cuisine], (-rating, food))
            self.ratings[food] = rating
            self.food_to_cuisine[food] = cuisine


    def changeRating(self, food: str, newRating: int) -> None:
        self.ratings[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heappush(self.pqs[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = self.pqs[cuisine][0]
            if -rating != self.ratings[food]:
                heappop(self.pqs[cuisine])
                continue
            return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
