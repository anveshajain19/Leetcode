class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans.append(nums[i])
        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                ans.append(nums[j])
        return ans
                
        