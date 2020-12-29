#https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_array = len(nums)
        index = len_array - 1
        left, right = 0, index
        result = [0 for num in nums]

        while index >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                result[index] = nums[left] * nums[left] 
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result