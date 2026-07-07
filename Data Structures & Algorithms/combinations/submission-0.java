class Solution {
    private void dfs(int[] nums, int i, int k, List<Integer> subset, List<List<Integer>> subsets) {
        if (subset.size() == k) {
            subsets.add(new ArrayList<>(subset));
            return;
        }

        if (i == nums.length) return;

        subset.add(nums[i]);
        dfs(nums, i + 1, k, subset, subsets);
        subset.remove(subset.size() - 1);
        dfs(nums, i + 1, k, subset, subsets);
    }

    public List<List<Integer>> combine(int n, int k) {
        int[] nums = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }

        List<List<Integer>> subsets = new ArrayList<>();
        dfs(nums, 0, k, new ArrayList<>(), subsets);
        return subsets;
    }
}