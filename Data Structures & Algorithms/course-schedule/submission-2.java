class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList();
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] prerequisite : prerequisites) {
            int dest = prerequisite[0];
            int src = prerequisite[1];

            adj.get(src).add(dest);
            inDegree[dest]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i); // Offer the index 'i', not the value '0'
            }
        }

        int finishCount = 0;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            finishCount++;

            for (Integer neighbor : adj.get(curr)) {
                inDegree[neighbor]--;

                if (inDegree[neighbor] == 0)
                    queue.offer(neighbor);
            }
        }

        return finishCount == numCourses;
    }
}
