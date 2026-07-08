class Solution {
    private void dfs(int[] nums, int start, List<Integer> subset, List<List<Integer>> subsets) {
        subsets.add(new ArrayList<>(subset));

        for (int i = start; i < nums.length; i++) {

            if (i > start && nums[i - 1] == nums[i]) {
                continue;
            }

            subset.add(nums[i]);
            dfs(nums, i + 1, subset, subsets);
            subset.remove(subset.size() - 1);
        }
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> subsets = new ArrayList<>();
        dfs(nums, 0, new ArrayList<>(), subsets);
        return subsets;
    }
}
