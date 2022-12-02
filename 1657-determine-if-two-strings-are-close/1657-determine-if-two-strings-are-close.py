class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
         return sorted(Counter(list(word1)).values()) == sorted(Counter(list(word2)).values()) and set(word1) == set(word2)
            
            
        