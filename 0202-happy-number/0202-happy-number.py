class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in store:
                return False
            else:
                store.add(n)
        else:
            return True
        
        