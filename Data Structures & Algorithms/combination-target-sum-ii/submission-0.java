class Solution {
    private void dfs(int[] candidates, int target, int i, List<Integer> subset, List<List<Integer>> subsets) {
        if (target == 0) {
            subsets.add(new ArrayList(subset));
            return;
        }

        if (i == candidates.length || target < 0 || target - candidates[i] < 0) {
            return;
        }


        subset.add(candidates[i]);
        dfs(candidates, target - candidates[i], i + 1, subset, subsets);
        subset.remove(subset.size() - 1);

        while (i + 1 < candidates.length && candidates[i] == candidates[i+1]) {
            i++;
        }
        dfs(candidates, target, i + 1, subset, subsets);
    }

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> subsets = new ArrayList();         
        Arrays.sort(candidates);
        dfs(candidates, target, 0, new ArrayList(), subsets);

        return subsets;
    }
}
