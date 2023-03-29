class Solution(object): 
    def buildAdjacencyList(self, n, edgesList):
        adjList = [[] for _ in range(n)]
        # c2 (course 2) is a prerequisite of c1 (course 1)
        # i.e c2c1 is a directed edge in the graph
        for c1, c2 in edgesList:
            adjList[c2].append(c1)
        return adjList

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # build Adjacency list from Edges list
        adjList = self.buildAdjacencyList(numCourses, prerequisites)
        print(adjList)
        visited = set()

        def hasCycle(v, stack):
            print("current:", v, ", visited: ", visited, ", stack: ", stack)
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            # mark this vertex as visited
            visited.add(v)
            # add it to the current stack
            stack.append(v)
            print("current:", v, ", visited: ", visited, ", stack: ", stack)

            for i in adjList[v]:
                if hasCycle(i, stack):
                    return True

            # once processed, we pop it out of the stack
            stack.pop()
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v, []):
                return False

        return True