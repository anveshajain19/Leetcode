class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = abs(int(sqrt(num)))
        return a*a == num