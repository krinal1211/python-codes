class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool """
        if len(s) != len(t):
            return False
        hash_s_to_t = {}
        hash_t_to_s = {}      
        for i, j in zip(s, t):
            if i in hash_s_to_t:
                if hash_s_to_t[i] != j:
                    return False
            else:
                hash_s_to_t[i] = j
            
            if j in hash_t_to_s:
                if hash_t_to_s[j] != i:
                    return False
            else:
                hash_t_to_s[j] = i           
        return True

            
