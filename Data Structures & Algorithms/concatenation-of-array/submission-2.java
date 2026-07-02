class Solution {
    public int[] getConcatenation(int[] nums) {
        int[] nums1 = new int[2 * nums.length];

        for (int i = 0; i < nums1.length; i++) {
            if (i < nums.length) {
                nums1[i] = nums[i];
            } else {
                nums1[i] = nums[i - nums.length];
            }
        }

        return nums1;
        
    }
}