# Difficulty level: easy

#  You are given an integer n representing the number of steps to reach the top of a staircase.
#  You can climb with either 1 or 2 steps at a time.

# Return the number of distinct ways to climb to the top of the staircase.


class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        numbers = [0] * (n + 1)

        numbers[1] = 1

        if n >= 2:
            numbers[2] = 2
            if n == 2:
                return 2
            
        for i in range(3, n + 1):
                numbers[i] = numbers[i - 1] + numbers[i - 2]
        return numbers[n]                
        