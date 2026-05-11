class Solution {
    public Map<Integer, List<Integer>> buildAdjacencyList(int n, int[][] edges) {
        Map<Integer, List<Integer>> adjacencyList = new HashMap<>();

        for (int[] edge: edges) {
            int u = edge[0];
            int v = edge[1];

            if (adjacencyList.containsKey(u)) {
                var neighbors = adjacencyList.get(u);
                neighbors.add(v);
            } else {
                var neighbors = new ArrayList();
                neighbors.add(v);
                adjacencyList.put(u, neighbors);
            }

            if (adjacencyList.containsKey(v)) {
                var neighbors = adjacencyList.get(v);
                neighbors.add(u);
            } else {
                var neighbors = new ArrayList();
                neighbors.add(u);
                adjacencyList.put(v, neighbors);
            }
        }

        return adjacencyList;
    }

    public void traverseComponent(int node, Set<Integer> visited, Map<Integer, List<Integer>> adjList) {
        if (visited.contains(node)) {
            return;
        }

        visited.add(node);

        for (Integer neighbor: adjList.get(node)) {
            traverseComponent(neighbor, visited, adjList);
        }
    }

    public int countComponents(int n, int[][] edges) {
        var adjList = buildAdjacencyList(n, edges);
        var visited = new HashSet<Integer>();
        var components = 0;
        for (int i = 0; i < n; i++) {
            if (!visited.contains(i)) {
                traverseComponent(i, visited, adjList);
                components++;
            }
        }

        return components;
    }
}
