class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = ((r+l) // 2)

        while pivot >= l:
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                r = pivot - 1
                pivot = ((r + l) // 2)
            else:
                l = pivot + 1
                pivot = ((r + l) // 2)
        if nums[pivot] == target:
            return pivot
        else:
            return -1