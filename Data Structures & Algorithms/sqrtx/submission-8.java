class Solution {
    public int mySqrt(int x) {
        int l = 1;
        int r = x;

        while (l <= r) {
            int m = l + (r - l) / 2;
            long num = (long) m * m;
            if (num == x) {
                return m;
            }

            if (num > x) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return r;
    }
}