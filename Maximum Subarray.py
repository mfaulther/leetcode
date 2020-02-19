#https://leetcode.com/problems/maximum-subarray
class Solution:
    
    def cross(self, arr, left, mid, right):
        left_sum = -500
        sum = 0
        for i in range(mid,left-1,-1):
           sum += arr[i]
           left_sum = max(left_sum, sum)
    
        right_sum = -500
        sum = 0
        for i in range(mid + 1, right+1):
           sum += arr[i]
           right_sum = max(right_sum, sum)
        return left_sum + right_sum
    
    
    
    def maxSubArray1(self, nums: List[int],left:int, right:int) -> int:
        if left == right:
            return nums[left]
        mid = (left + right)//2
        left_sum = self.maxSubArray1(nums,left,mid)
        right_sum = self.maxSubArray1(nums,mid + 1, right)
        cross_sum = self.cross(nums,left,mid,right)
        return max(left_sum, right_sum, cross_sum)
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArray1(nums,0,len(nums)-1)