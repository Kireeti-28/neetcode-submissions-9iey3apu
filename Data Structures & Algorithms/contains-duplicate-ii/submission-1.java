class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        int n = nums.length;
        Set<Integer> window = new HashSet();
        int l = 0;
        int r = 0;

        while (r < n) {
            window.add(nums[r]);
            int curWindowSize = r - l + 1;

            if (curWindowSize != window.size()) return true;

            if (curWindowSize == k + 1) {
                window.remove(nums[l]);
                l++;
            }

            r++;
        }

        return false;
    }
}