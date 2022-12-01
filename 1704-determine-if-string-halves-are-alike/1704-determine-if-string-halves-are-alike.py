class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vow = set('aeiouAEIOU')
        sumA = sumB = 0
        for i in range(len(s)//2):
            if s[i] in vow:
                sumA += 1
            if s[len(s)//2+i] in vow:
                sumB += 1
        return sumA == sumB
        