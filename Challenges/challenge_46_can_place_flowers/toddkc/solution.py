class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #if no flowers to be planted
        if n == 0: return True

        #if flowerbed only has one spot and is taken
        if len(flowerbed) == 1:
            return False if flowerbed[0] == 1 else True

        remaining = n
        #handle first
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            remaining -= 1
        #handle last
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[len(flowerbed)-1] = 1
            remaining -= 1
        #handle middle
        for i in range(1, len(flowerbed) - 1):
            if remaining == 0: return True
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                remaining -= 1
        if remaining <= 0: return True
        return False
