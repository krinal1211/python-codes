class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        
        max_length = 0
        start = 0
        current_cost = 0
        
        for end in range(n):
            current_cost += cost[end]
            
            while current_cost > maxCost:
                current_cost -= cost[start]
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length
