class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l =0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
        return nums
    

nums = [0, 1, 0, 3, 12]
cls_obj = Solution()
print(cls_obj.moveZeroes(nums))


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Moves all zeros in the list to the end while maintaining the order of non-zero elements.
        This solution overwrites non-zero elements in-place, then fills the rest with zeros.
        Time Complexity: O(n), Space Complexity: O(1)
        """
        insert_pos = 0
        # Move all non-zero elements to the front
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        # Fill the rest with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        return nums
class_obj2 = Solution2()
nums2 = [0, 1, 0, 3, 12]
print(class_obj2.moveZeroes(nums2))
