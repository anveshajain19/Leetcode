class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = []
        yo = []
        for i in range(len(num)):
            a.append(str(num[i]))
        ans = ''.join(a)
        final = str(int(ans) + k)
        for i in range(len(final)):
            yo.append(int(final[i]))
        return yo
            
            
        