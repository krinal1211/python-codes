class Solution(object):
    def removeKdigits(self, num, k):
        stack = []    
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)     
        while k > 0:
            stack.pop()
            k -= 1      
        output = ''.join(stack).lstrip('0')       
        if not output:
            return '0'       
        return output
