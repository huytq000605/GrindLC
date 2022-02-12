from sortedcontainers import SortedList

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.rented = SortedList()
        self.movies = defaultdict(SortedList)
        self.prices = defaultdict(dict)
            
        for shop, movie, price in entries:
            self.movies[movie].add((price, shop))
            self.prices[shop][movie] = price
        

    def search(self, movie: int) -> List[int]:
        return list(map(lambda ele: ele[1], self.movies[movie][:5]))

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.movies[movie].discard((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices[shop][movie]
        self.movies[movie].add((price, shop))
        self.rented.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        return list(map(lambda ele: [ele[1], ele[2]], self.rented[:5]))


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()