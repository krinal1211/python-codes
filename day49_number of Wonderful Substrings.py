class Solution(object):
    def wonderfulSubstrings(self, word):
        cnt = 0
        n = len(word)
        fmap = {0: 1}
        mask = 0
        
        for i in range(n):
            idx = ord(word[i]) - ord('a')
            mask ^= 1 << idx
            cnt += fmap.get(mask, 0)
            for j in range(10):
                p_mask = mask ^ (1 << j)
                cnt += fmap.get(p_mask, 0)
            fmap[mask] = fmap.get(mask, 0) + 1
        
        return cnt
