class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        count = 0
        while i < j:
            current_sum = nums[i] + nums[j]
            if current_sum == k:
                count += 1
                nums.pop(j)
                nums.pop(i)
                j -= 2
            elif current_sum < k:
                i += 1
            else:
                j -= 1
        return count


sol = Solution()
print(sol.maxOperations([1, 2, 3, 4], 5))
print(sol.maxOperations([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2))
