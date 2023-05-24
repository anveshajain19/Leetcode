class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            binary_str = bin(i)[2:]
            for char in binary_str:
                if char == '1':
                    count += 1
            ans.append(count)
        return ans
