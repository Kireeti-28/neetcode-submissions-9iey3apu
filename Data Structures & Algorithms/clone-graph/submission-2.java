/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    private Node dfs(Node node, Map<Node, Node> oldToNew) {
        if (node == null)
            return null;

        if (oldToNew.containsKey(node)) {
            return oldToNew.get(node);
        }

        Node nodeCopy = new Node(node.val);
        oldToNew.put(node, nodeCopy);

        for (Node neighbor : node.neighbors) {
            nodeCopy.neighbors.add(dfs(neighbor, oldToNew));
        }

        return nodeCopy;
    }
    public Node cloneGraph(Node node) {
        return dfs(node, new HashMap<>());
    }
}