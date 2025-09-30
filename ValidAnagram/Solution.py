class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        if len(s) != len(t):
            return False
        
        for c in s:
            val = dict.get(c, 0)
            dict[c] = val + 1
        
        for c in t:
            val = dict.get(c, 0)
            dict[c] = val - 1

        for _, v in dict.items():
            if v != 0:
                return False
        return True