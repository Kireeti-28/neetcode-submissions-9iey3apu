class Solution {
    private void dfs(int n, int opens, int closes, StringBuilder sb, List<String> parenthesis) {
        if (opens == n && closes == n) {
            parenthesis.add(sb.toString());
            return;
        }

        if (opens + closes == 2 * n) {
            return;
        }

        if (opens < n) {
            sb.append("(");
            dfs(n, opens + 1, closes, sb, parenthesis);
            sb.deleteCharAt(sb.length() - 1);
        }
        
        if (opens > closes) {
            sb.append(")");
            dfs(n, opens, closes + 1, sb, parenthesis);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public List<String> generateParenthesis(int n) {
        List<String> parenthesis = new ArrayList();
        dfs(n, 0, 0, new StringBuilder(), parenthesis);
        return parenthesis;
    }
}
