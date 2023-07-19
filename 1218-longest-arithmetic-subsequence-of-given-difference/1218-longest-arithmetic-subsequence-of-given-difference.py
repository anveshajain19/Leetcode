class Solution:
    def longestSubsequence(self, a: List[int], d: int) -> int:
        dp = defaultdict(int)
        for x in a:
                dp[x] = dp[x-d] + 1
        return max(dp.values())