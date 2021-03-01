"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

"""
class Solution:
    v=0
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        mid = int(n/2)
        
        #corners
        if n==1:
            return self.v
        
        if n>=2:
            if nums[n-1]>nums[n-2]:
                self.v += n-1
                return self.v
            if nums[0]>nums[1]:
                return self.v
            
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            self.v += mid
            return self.v
        
        if nums[mid-1]>nums[mid]:
            self.v+=0
            return self.findPeakElement(nums[0:mid])
        if  nums[mid+1]>nums[mid]:
            self.v += mid
            return self.findPeakElement(nums[mid::])
            
 solution = Solution()
 l= [1,2,1,3,5,6,4]
 solution.findPeakElement(l)
