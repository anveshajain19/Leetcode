class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap and i - hashmap[s[i]] - 1 != distance[ord(s[i]) - ord('a')]:
                return False
            hashmap[s[i]] = i
        return True
            
        
                