class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        s = []
        
        while (r > l):

            if numbers[l] + numbers[r] == target:
                s.append(l + 1)
                s.append(r + 1)
                break
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -=1
        
        return s