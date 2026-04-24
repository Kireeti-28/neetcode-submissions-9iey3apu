class Solution {
    public List<String> getNeighbors(String node) {
        List<String> neighbors = new ArrayList();
        char[] chars = node.toCharArray();
        for (int i = 0; i < 4; i++) {
            char original = chars[i];

            chars[i] = (char) ((original - '0' + 1) % 10 + '0');
            neighbors.add(new String(chars));

            chars[i] = (char) ((original - '0' - 1 + 10) % 10 + '0');
            neighbors.add(new String(chars));

            chars[i] = original;
        }

        return neighbors;
    }
    public int openLock(String[] deadends, String target) {
    Set<String> visited = new HashSet<>(Arrays.asList(deadends));
    
    // Edge case: if start is a deadend, we can't move
    if (visited.contains("0000")) return -1;
    
    Queue<String> queue = new LinkedList<>();
    queue.offer("0000");
    visited.add("0000");
    
    int turns = 0;
    
    while (!queue.isEmpty()) {
        int size = queue.size(); // Process all nodes at the current level
        
        for (int i = 0; i < size; i++) {
            String current = queue.poll();
            
            if (current.equals(target)) return turns;
            
            // Get all 8 neighbors using the helper we discussed
            for (String neighbor : getNeighbors(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        turns++; // Increment turn count after processing the level
    }
    
    return -1; // Target unreachable
}
}