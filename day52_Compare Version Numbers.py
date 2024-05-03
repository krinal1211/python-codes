class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split('.')
        b = version2.split('.')       
        i = 0
        while i < len(a) or i < len(b):
            num1 = int(a[i]) if i < len(a) else 0
            num2 = int(b[i]) if i < len(b) else 0         
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            i += 1        
        return 0

            

        
