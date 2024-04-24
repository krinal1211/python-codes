class Solution(object):
    def openLock(self, deadends, target):
        dead = set(deadends)  
        if "0000" in dead:  
            return -1

        q = [('0000', 0)]  
        visited = set(['0000'])  
        front = 0  

        while front < len(q):  
            curr, moves = q[front]  
            front += 1  
            
            if curr == target:  
                return moves
            
            for i in range(4):  
                for d in (1, -1):  
                    new_dig = (int(curr[i]) + d) % 10  
                    new_comb = curr[:i] + str(new_dig) + curr[i+1:]  

                    if new_comb not in visited and new_comb not in dead:
                        visited.add(new_comb)  
                        q.append((new_comb, moves + 1))  

        return -1  
