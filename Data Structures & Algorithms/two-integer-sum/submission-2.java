class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mp = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            int want = target - nums[i];
            if (mp.containsKey(want)) return new int[]{mp.get(want), i};

            mp.put(nums[i], i);
        }

        return new int[]{-1, -1};
    }
}
