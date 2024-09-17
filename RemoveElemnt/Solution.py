
# Difficulty level: easy


class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

def main():
    # Create an instance of Solution
    sol = Solution()

    # Example 1: Removing elements
    nums = [3, 2, 2, 3]
    val = 3
    print(f"Original list: {nums}, Value to remove: {val}")
    result = sol.removeElement(nums, val)
    print(f"Number of elements left: {result}\n")


if __name__ == "__main__":
    main()



        