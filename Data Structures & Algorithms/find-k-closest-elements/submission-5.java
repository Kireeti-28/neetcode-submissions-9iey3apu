class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int n = arr.length;
        int[] diff = new int[n];
        for (int i = 0; i < n; i++) {
            diff[i] = Math.abs(arr[i] - x);
        }

        System.out.println(Arrays.toString(diff));

        int l = 0, r = 0, sums = 0;
        int minSum = Integer.MAX_VALUE;
        int minL = 0, minR = 0;

        while (r < n) {
            sums += diff[r];

            if (r - l + 1 == k) {
                if (sums < minSum) {
                    minL = l;
                    minR = r;
                    minSum = sums;
                }

                sums -= diff[l];
                l++;
            }

            r++;
        }

        List<Integer> ans = new ArrayList();
        for (int i = minL; i <= minR; i++) {
            ans.add(arr[i]);
        }

        return ans;
    }
}