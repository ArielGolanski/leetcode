# Difficulty level: medium

#  You are given an array of length n which was originally sorted in ascending order.
#  It has now been rotated between 1 and n times.
#  For example, the array nums = [1,2,3,4,5,6] might become:

#  [3,4,5,6,1,2] if it was rotated 4 times.
#  [1,2,3,4,5,6] if it was rotated 6 times.
#  Notice that rotating the array 4 times moves the last four elements
#  of the array to the beginning. Rotating the array 6 times produces the original array.

# Assuming all elements in the rotated sorted array nums are unique,
#  return the minimum element of this array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        

        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])    
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res                   
        
                

