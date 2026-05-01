class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t.lower()
        return sorted(s) == sorted(t)
        