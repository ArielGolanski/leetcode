# Difficulty level: medium

# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        myDict = {key:0 for key in nums}
        for num in nums:
            myDict[num] += 1
        for i in range(0, k):
            max = 0
            maxKey = None
            for key, value in myDict.items():
                if value > max:
                    max = value
                    maxKey = key
            myDict[maxKey] = 0
            res.append(maxKey)
        return res