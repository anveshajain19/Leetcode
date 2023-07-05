class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = 0
        strr = "".join([str(i) for i in nums])
        ones = strr.split("0")
        if len(ones) == 1:
            return len(nums) - 1
        lens = [len(one) for one in ones]
        for i in range(len(lens) - 1):
            m = max(m, lens[i] + lens[i + 1])
        return m
            