from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for str in strs:
            arr = [0] * 26
            for char in str:
                arr[ord(char) - ord("a")] += 1
            dict[tuple(arr)].append(str)
        
        return list(dict.values())