class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
    

# Example usage
nums = [5,5,2, 2, 1, 1, 1, 2, 2]
cls_obj = Solution()
print(cls_obj.majorityElement(nums))