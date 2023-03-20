class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        can = 0
        m = len(flowerbed)
        for f in range(m):
            if (f == 0 or not flowerbed[f-1]) and (f == m-1 or not flowerbed[f+1]):
                can += 1 - flowerbed[f]
                flowerbed[f] = 1
        return can >= n
