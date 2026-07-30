class Solution {
    private int helper(int i, int j, String text1, String text2) {
        if (i >= text1.length() || j >= text2.length()) return 0;

        int res = 0;
        if (text1.charAt(i) == text2.charAt(j)) {
            res = 1 + helper(i + 1, j + 1, text1, text2);
        } else {
            res = helper(i + 1, j, text1, text2);
        }

        return res;
    }
    public int longestCommonSubsequence(String text1, String text2) {
        return helper(0, 0, text1, text2);
    }
}
