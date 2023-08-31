class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev2 = 0
        prev = 1
        for i in range(2, n + 1):
            cur_i = prev2 + prev
            prev2 = prev
            prev = cur_i
        return prev
