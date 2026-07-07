class Solution {
    public void helper(int[] nums, int i, List<Integer> subset, List<List<Integer>> subsets) {
        if (i == nums.length) {
            subsets.add(new ArrayList(subset));
            return;
        }

        subset.add(nums[i]);
        helper(nums, i + 1, subset, subsets);
        subset.remove(subset.size() - 1);
        helper(nums, i + 1, subset, subsets);
    }

    public int xorSum(List<Integer> subset) {
        if (subset.size() == 0) return 0;

        int res = 0;

        for (int num: subset) {
            res = res ^ num;
        }

        return res;
    }

    public int subsetXORSum(int[] nums) {
        List<List<Integer>> subsets = new ArrayList();

        helper(nums, 0, new ArrayList(), subsets);

        int ans = 0;
        for (List<Integer> subset: subsets) {
            ans += xorSum(subset);
        }

        return ans;
    }
}