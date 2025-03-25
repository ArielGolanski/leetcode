class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index, num in enumerate(nums):
            if(dict.get(num) == None):
                dict[target - num] = index
            else:
                return [dict.get(num), index] 