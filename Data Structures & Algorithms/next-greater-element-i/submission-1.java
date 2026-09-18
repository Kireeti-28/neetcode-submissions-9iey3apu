class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] ans = new int[nums1.length];
        Arrays.fill(ans, -1);

        HashMap<Integer, Integer> mp = new HashMap();

        for (int i = 0; i < nums2.length; i++) {
            mp.put(nums2[i], i);
        }

        for (int i = 0; i < nums1.length; i++) {
            int j = mp.get(nums1[i]);

            for (int jj = j; jj < nums2.length; jj++) {
                if (nums2[jj] > nums1[i]) {
                    ans[i] = nums2[jj];
                    break;
                }
            }
        }

        return ans;
        
    }
}