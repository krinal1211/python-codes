class Solution(object):
    def findRotateSteps(self, ring, key):
        memo = {}
        
        def dp(index_ring, index_key):
            if index_key == len(key):
                return 0
            if (index_ring, index_key) in memo:
                return memo[(index_ring, index_key)]
            
            result = float('inf')
            for i in range(len(ring)):
                if ring[i] == key[index_key]:
                    cWise = abs(index_ring - i)
                    cCwise = len(ring) - cWise
                    steps = min(cWise, cCwise)
                    result = min(result, steps + dp(i, index_key + 1))
            
            memo[(index_ring, index_key)] = result
            return result
        
        return dp(0, 0) + len(key)
