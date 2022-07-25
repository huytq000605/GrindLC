from sortedcontainers import SortedList

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_convert = defaultdict(SortedList)
        self.food_convert = dict()
        n = len(foods)
        for i in range(n):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            self.food_convert[food] = (cuisine, rating)
            self.cuisine_convert[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, rating = self.food_convert[food]
        self.cuisine_convert[cuisine].remove((-rating, food))
        self.food_convert[food] = (cuisine, newRating)
        self.cuisine_convert[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_convert[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
