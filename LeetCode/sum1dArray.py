#https://leetcode.com/problems/running-sum-of-1d-array
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         sum = 0
#         result = list()
#         for i in range(1, len(nums)):
#             sum += nums[i];
#             result.append(sum)
#         return result

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums