https://leetcode.com/problems/two-sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            x = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == target - x:
                    return [i,j]