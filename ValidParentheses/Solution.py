class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                c+=1
            else:
                if s[i] == ')':
                    if c == 0:
                        return False
                    elif stack.pop() != '(':
                        return False
                    else:
                        c-=1
                elif s[i] == '}':
                    if c == 0:
                        return False
                    elif stack.pop() != '{':
                        return False
                    else:
                        c-=1
                else:
                    if c == 0:
                        return False
                    elif stack.pop() != '[':
                        return False
                    else:
                        c-=1
        if c != 0:
            return False
        else:
            return True