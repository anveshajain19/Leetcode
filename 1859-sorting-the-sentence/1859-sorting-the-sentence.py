
class Solution:
    def sortSentence(self, s: str) -> str:
        words = [word[:-1] for word in sorted(s.split(), key = lambda x:x[-1])]
        return ' '.join(words)