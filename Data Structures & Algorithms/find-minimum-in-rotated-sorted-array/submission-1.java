class Solution {
    public int findMin(int[] nums) {
        int l = 0;
        int r = nums.length - 1;

        while (l < r) {
            int m = (r - l) + l / 2;

            if (nums[l] < nums[m]) { // left sorted
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return nums[l];
    }
}
