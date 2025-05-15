class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j,nums[:j]

nums = [1, 1, 2,3,3,4,5,5]
cls_obj = Solution()
print(cls_obj.removeDuplicates(nums))