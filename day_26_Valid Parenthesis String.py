class Solution(object):
    def checkValidString(self, s):
        stack = []
        star = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                star.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
        
        while stack:
            if not star:
                return False
            
            if stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                return False
        
        return True
