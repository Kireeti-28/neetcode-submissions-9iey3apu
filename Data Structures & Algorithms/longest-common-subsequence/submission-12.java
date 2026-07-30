class Solution {
    private int helper(int i, int j, String text1, String text2, int[][] dp) {
        if (i >= text1.length() || j >= text2.length()) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        int res = 0;
        if (text1.charAt(i) == text2.charAt(j)) {
            res = 1 + helper(i + 1, j + 1, text1, text2, dp);
        } else {
            res = Math.max(helper(i, j + 1, text1, text2, dp), helper(i + 1, j, text1, text2, dp));
        }

        dp[i][j] = res;

        return dp[i][j];
    }
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        int[][] dp = new int[m + 1][n + 1];
        for (int[] row: dp) {
            Arrays.fill(row, -1);
        }

        helper(0, 0, text1, text2, dp);
        return dp[0][0];
    }
}
