class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        curr = 0
        a = 0
        b = int(c ** (0.5))
        while a <= b:
            curr = a * a + b * b
            if curr == c:
                return True
            elif curr < c:
                a += 1
            else:
                b -= 1
        return False



