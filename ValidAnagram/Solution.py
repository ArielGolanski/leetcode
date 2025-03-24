class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        
        for i in range(len(s)):
            if dict.get(s[i]) == None:
                dict[s[i]] = 1
            else:
                dict[s[i]] = dict[s[i]] + 1
        
        for i in range(len(t)):
            if dict.get(t[i]) == None:
                return False
            else:
                dict[t[i]] = dict[t[i]] - 1
                
        for i in range(len(s)):
            if dict.get(s[i]) != 0:
                return False
        return True