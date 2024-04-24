class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]  
    
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        leaves = [node for node in range(n) if len(adj[node]) == 1]
        
        while n > 2:
            n -= len(leaves)  
            new_leaves = []
            for leaf in leaves:
                neig = adj[leaf].pop()  
                adj[neig].remove(leaf)  
                if len(adj[neig]) == 1:
                    new_leaves.append(neig)  
            leaves = new_leaves
        
        return leaves
