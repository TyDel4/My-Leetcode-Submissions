from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for i in range(len(s)):
            if(len(stack) == 0):
                stack.append(s[i])
            else:
                match s[i]:
                    case '(' | '[' | '{':
                        stack.append(s[i])
                    case ')':
                        if stack.pop() != '(':
                            return False
                    case '}':
                        if stack.pop() != '{':
                            return False
                    case ']':
                        if stack.pop() != '[':
                            return False
        if len(stack) != 0:
            return False
        return True
    