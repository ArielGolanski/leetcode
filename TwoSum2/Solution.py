# Difficulty level: medium


# Given an array of integers numbers that is sorted in non-decreasing order.

#  Return the indices (1-indexed) of two numbers,
#  [index1, index2], such that they add up to a given target number target and index1 < index2.
#  Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use O(1) additional space.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 1
        e = len(numbers)

        while(s < e):
            if(numbers[s - 1] + numbers[e - 1] == target):
                return [s, e]
            elif (numbers[s - 1] + numbers[e - 1] > target):
                e -= 1
            else:
                s += 1
        return []            