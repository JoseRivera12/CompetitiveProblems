#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in s:
                return [s[other], index]
            s[num] = index
        return []



