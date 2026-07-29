class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        size = len(flowerbed)
        i = 0
        next = 0
        while i < size:
            if n == 0:
                return True
            if i + 1 <= size - 1:
                next = i + 1
            if flowerbed[i] == 1:
                i += 2
                continue
            if flowerbed[i] == 0 and flowerbed[next] == 0:
                flowerbed[i] = 1
                n -= 1
                i = i + 2
                continue
            i += 1
        return False


sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(sol.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
print(sol.canPlaceFlowers([0, 1, 0], 1))
print(sol.canPlaceFlowers([0, 0, 1, 0, 1], 1))
print(sol.canPlaceFlowers([0, 0, 1, 0, 0], 1))
