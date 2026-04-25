class Solution {
    public boolean isCyclic(int node, Map<Integer, List<Integer>> adjList, Set<Integer> visited) {
        if (visited.contains(node)) {
            return true;
        }
        if (adjList.getOrDefault(node, new ArrayList<>()).isEmpty()) return false;

        visited.add(node);

        for (int neighbor: adjList.get(node)) {
            if (isCyclic(neighbor, adjList, visited)) {
                return true;
            }
        }

        visited.remove(node);

        return false;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> adjList = new HashMap();

        for (int[] course: prerequisites) {
            int u = course[1];
            int v = course[0];

            if (adjList.containsKey(v)) {
                var neighbors = adjList.get(v);
                neighbors.add(u);
                adjList.put(v, neighbors);
            } else {
                var neighbors = new ArrayList();
                neighbors.add(u);
                adjList.put(v, neighbors);
            }
        }

        for (int i = 0; i < numCourses; i++) {
            if (isCyclic(i, adjList, new HashSet())) return false;
        }
        return true;

    }
}
