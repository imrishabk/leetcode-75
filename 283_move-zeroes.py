class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)


sol = Solution()
print(sol.moveZeroes([0, 1, 0, 3, 12]))
print(sol.moveZeroes([0]))
print(sol.moveZeroes([1, 0, 0, 3, 12]))
print(sol.moveZeroes([1, 1, 1, 0, 0]))
print(sol.moveZeroes([1, 0, 1, 0, 2, 0, 1]))
print(sol.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))
