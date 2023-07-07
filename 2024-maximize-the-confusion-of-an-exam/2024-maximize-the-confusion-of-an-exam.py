class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = j = 0
        res = 0
        d = dict()
        while i < len(answerKey):
            d[answerKey[i]] = d.get(answerKey[i],0) + 1
            while d.get("T",0) > k and d.get("F",0) > k:
                res = max(res, i-j)
                d[answerKey[j]] -= 1
                j += 1
            i += 1
        return max(res, i-j)