class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            water = min(height[i], height[j]) * (j - i)
            res = max(res, water)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return res
