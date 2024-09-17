# Difficulty level: medium

#  You are given an array of strings tokens that represents
#  a valid arithmetic expression in Reverse Polish Notation.

# Return the integer that represents the evaluation of the expression.

# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array = []
        for c in tokens:
            if (c != "+" and c != "-" and c != "*" and c != "/"):
                array.append(c)
            else:
                right = array.pop()
                left = array.pop()

                if c == "+":
                    result = int(left) + int(right)
                    array.append(str(result))
                elif c == "-":
                    result = int(left) - int(right)
                    array.append(str(result))
                elif c == "*":
                    result = int(left) * int(right)
                    array.append(str(result))
                else:
                    if right == 0:
                        raise ZeroDivisionError("Division by zero encountered!")
                    else:
                        result = int(left) / int(right)
                        array.append(str(int(result)))
        return int(array.pop())                