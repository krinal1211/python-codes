class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        a = set()

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    a.add(i)
        a.update(stack)
        result = ''
        for i in range(len(s)):
            char = s[i]
            if i not in a:
                result += char

        return result
        
