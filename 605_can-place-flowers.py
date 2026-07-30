class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        size = len(flowerbed)
        for i in range(size):
            if i == 0 and flowerbed[i] == 1:
                continue
            if i + 1 <= size - 1 and flowerbed[i + 1] == 1:
                continue
            if i - 1 >= 0 and flowerbed[i - 1] == 1:
                continue
            if flowerbed[i] == 1:
                continue
            n -= 1
            flowerbed[i] = 1
            print(flowerbed)
            if n == 0:
                return True
        return False


sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(sol.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
print(sol.canPlaceFlowers([0, 1, 0], 1))
print(sol.canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))
