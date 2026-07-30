class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res: list[int] = [1] * length
        for i in range(1, length):
            res[i] = nums[i - 1] * res[i - 1]
        backtracker = 1
        for i in range(length - 1, -1, -1):
            res[i] *= backtracker
            backtracker *= nums[i]
        return res


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
