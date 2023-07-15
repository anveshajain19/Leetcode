class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for l1, l2 in zip(word1, word2):
            ans += l1 + l2
        diff = len(word1) - len(word2)
        if diff >0:
            ans += word1[-diff:]
        elif diff < 0:
            ans+= word2[diff:]
        return ans
            