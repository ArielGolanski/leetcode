class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for key in nums:
            val = dict.get(key, 0)
            dict[key] = val + 1
            if dict.get(key, 0) > 1:
                return True
        return False