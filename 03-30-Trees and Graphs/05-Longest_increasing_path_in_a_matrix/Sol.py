# * A cell in the matrix as a node,
# * A directed edge from node x to node y if x and y are adjacent and x's value < y's value

# A graph is formed.
# No cycles can exist in the graph, i.e. a DAG is formed.

# The problem becomes to get the longest path in the DAG.
# Topological sort can iterate the vertices of a DAG in the linear ordering.
# Using Kahn's algorithm (BFS) to implement topological sort while counting the levels can give us the longest chain of nodes in the DAG.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        if rows == 0:
            return 0
        
        cols = len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)] 
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        for x in range(rows):
            for y in range(cols):
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] < matrix[x][y]:
                            indegree[x][y] += 1
                            
        queue = []
        for x in range(rows):
            for y in range(cols):
                if indegree[x][y] == 0:
                    queue.append((x, y))
    
        path_len = 0
        while queue:
            sz = len(queue)
            for i in range(sz):
                x, y = queue.pop(0)
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]
                    if nx >= 0 and ny >= 0 and nx < rows and ny < cols:
                        if matrix[nx][ny] > matrix[x][y]:
                            indegree[nx][ny] -= 1
                            if indegree[nx][ny] == 0:
                                queue.append((nx, ny))
            path_len += 1
        return path_len