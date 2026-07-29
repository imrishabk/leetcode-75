class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candy = max(candies)
        return [c + extraCandies >= max_candy for c in candies]


sol = Solution()
print(sol.kidsWithCandies([12, 1, 12], 10))
print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))
