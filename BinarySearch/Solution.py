# Difficulty level: easy

# You are given an array of distinct integers nums, sorted in ascending order,
#  and an integer target.

#  Implement a function to search for target within nums.
#  If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn) time.


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1           


