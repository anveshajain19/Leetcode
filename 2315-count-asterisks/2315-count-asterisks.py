class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([chars.count("*") for chars in s.split('|')][0::2])