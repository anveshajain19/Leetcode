class Solution:
    def alternateDigitSum(self, n: int) -> int:
        a = str(n)
        digit_sum = 0
        for i in range(len(a)):
            digit = int(a[i])
            sign = (-1) ** i 
            digit_sum += sign * digit
        return digit_sum
