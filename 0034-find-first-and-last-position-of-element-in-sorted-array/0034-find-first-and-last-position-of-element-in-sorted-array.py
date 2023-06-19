class Solution:
    def searchRange(self, nums, target):
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
    
    def binarySearch(self, nums, target, isLeft):
        left = 0
        right = len(nums) - 1
        index = -1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (isLeft and nums[mid] == target):
                right = mid - 1
            else:
                left = mid + 1
            
            if nums[mid] == target:
                index = mid
        
        return index
