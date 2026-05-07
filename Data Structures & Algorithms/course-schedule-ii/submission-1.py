class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
        
        queue = deque([ i for i in range(numCourses) if indegree[i] == 0])
        ans = []
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(ans) == numCourses:
            return ans
        
        return []