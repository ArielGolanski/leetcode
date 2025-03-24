class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict ={}
        
        for index, num in enumerate(nums):
            if dict.get(num) != None:
                return True
            else:
                dict[num] = index
        return False