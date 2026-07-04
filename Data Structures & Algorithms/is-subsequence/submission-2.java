class Solution {
    public boolean helper(String s, String t, int i, int j) {
        // System.out.println()
        if (i == s.length()) return true;

        if (j == t.length()) return false;

        boolean passOne = s.charAt(i) == t.charAt(j) && helper(s, t, i + 1, j + 1);
        boolean passTwo = helper(s, t, i, j + 1);

        return passOne || passTwo;

    }
    public boolean isSubsequence(String s, String t) {
        if (t.length() < s.length()) return false;

        return helper(s, t, 0, 0);
    }
}