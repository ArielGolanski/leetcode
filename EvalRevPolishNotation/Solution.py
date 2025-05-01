class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 - val2)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(float(val1) / int(val2)))
            else:
                stack.append(int(c))
        return stack.pop()