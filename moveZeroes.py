"""
Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

- Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                
if __name__ == '__main__':
    obj = Solution()
    arr = [0,1,0,3,12]
    obj.moveZeroes(arr)
    print(arr)
