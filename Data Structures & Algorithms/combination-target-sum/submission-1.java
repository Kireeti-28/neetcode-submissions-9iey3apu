class Solution {
    public void dfs(int[] nums, int target, int i, List<Integer> subset, List<List<Integer>> subsets) {
        if (target == 0) {
            subsets.add(new ArrayList(subset));
            return;
        }

        if (target < 0 || i == nums.length) {
            return;
        }

        subset.add(nums[i]);
        dfs(nums, target - nums[i], i, subset, subsets);
        subset.remove(subset.size() - 1);
        dfs(nums, target, i + 1, subset, subsets);
    }

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> subsets = new ArrayList();
        dfs(nums, target, 0, new ArrayList(), subsets);
        return subsets;
    }
}
