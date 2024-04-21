class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
       
        adj_list = {}
        for edge in edges:
            if edge[0] not in adj_list:
                adj_list[edge[0]] = []
            if edge[1] not in adj_list:
                adj_list[edge[1]] = []
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        visited = set()
        queue = [source]
        visited.add(source)     
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex == destination:
                return True
            for neighbor in adj_list[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)     
        return False


