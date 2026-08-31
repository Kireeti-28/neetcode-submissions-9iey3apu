class Solution {
    public int majorityElement(int[] nums) {
        int majEle = Integer.MIN_VALUE;
        int majCnt = 0;

        for (int i = 0; i < nums.length; i++) {
            if (majCnt == 0) {
                majEle = nums[i];
                majCnt = 1;
            }else if (nums[i] == majEle) {
                majCnt++;
            } else {
                majCnt--;
            }
        }

        return majEle;
    }
}