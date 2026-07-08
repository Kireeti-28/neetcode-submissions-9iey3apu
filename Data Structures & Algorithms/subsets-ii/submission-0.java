class Solution {
    public void dfs(int[] nums, int idx, List<Integer> subset, List<List<Integer>> subsets) {
        if (idx == nums.length) {
            subsets.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[idx]);
        dfs(nums, idx + 1, subset, subsets);
        subset.remove(subset.size() - 1);

        while (idx + 1 < nums.length && nums[idx] == nums[idx + 1]) {
            idx++;
        }
        dfs(nums, idx + 1, subset, subsets);
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> subsets = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), subsets);
        return subsets;
    }
}
