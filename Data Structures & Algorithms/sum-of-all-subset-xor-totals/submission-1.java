class Solution {
    private int totalXORSum = 0;
    
    public void helper(int[] nums, int i, int xorSum) {
        if (i == nums.length) {
            totalXORSum += xorSum;
            return;
        }

        helper(nums, i + 1, xorSum ^ nums[i]);
        helper(nums, i + 1, xorSum);
    }

    public int subsetXORSum(int[] nums) {
        helper(nums, 0, 0);

        return totalXORSum;
    }
}