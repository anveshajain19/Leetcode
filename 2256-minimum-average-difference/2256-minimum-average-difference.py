class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        i, m = 0, inf                       
        pfx, sfx = 0, sum(nums)              
        for j,n in enumerate(nums,start=1):
            pfx, sfx = pfx+n, sfx-n          
            k = len(nums)-j or 1             
            d = abs(pfx//j - sfx//k)
            if d < m:
                m, i = d, j-1
        return i