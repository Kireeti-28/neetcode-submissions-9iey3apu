class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for dest, src in prerequisites:
            adj[src].append(dest)
            inDegree[dest] += 1
        
        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        finishCount = 0

        while queue:
            curr = queue.popleft()
            finishCount += 1
             
            for neighbor in adj[curr]:
                inDegree[neighbor] -= 1

                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return finishCount == numCourses
