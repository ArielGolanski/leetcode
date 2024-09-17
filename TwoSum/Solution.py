# Difficulty level: easy

# Given an array of integers nums and an integer target,
# return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices
#  i and j that satisfy the condition.

# Return the answer with the smaller index first.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in index_map:
                return [index_map[complement], i]
            index_map[num] = i
        return []


def main():
    # Create an instance of Solution
    sol = Solution()

    # Example 1: Removing elements
    nums = [2, 4, 3]
    target = 5
    result = sol.twoSum(nums, target)
    print(f"{result}\n")


if __name__ == "__main__":
    main()