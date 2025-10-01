class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        s = []

        for index, num in enumerate(nums):
            
            val = dict.get(num, -1)

            if val >= 0:
                s.append(val)
                s.append(index)
                return s

            dict[target - num] = index
