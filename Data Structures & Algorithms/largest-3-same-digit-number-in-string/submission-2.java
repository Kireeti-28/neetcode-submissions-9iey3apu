class Solution {
    public String largestGoodInteger(String num) {
        char maxDigit = '/';
        int n = num.length();

        for (int i = 0; i < n - 2; i++) {
            if (num.charAt(i) == num.charAt(i + 1) && num.charAt(i + 1) == num.charAt(i + 2)) {
                if (num.charAt(i) > maxDigit) {
                    maxDigit = num.charAt(i);
                }
            }
        }

        return maxDigit == '/' ? "" : String.valueOf(maxDigit).repeat(3);
    }
}