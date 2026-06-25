class Solution {
    public int countOdds(int low, int high) {
        int cnt = 0;

        while (low <= high) {
            if (low == high && low % 2 == 1 && high % 2 == 1) {
                cnt++;
                break;
            }

            if (low % 2 == 1) cnt++;

            if (high % 2 == 1) cnt++;

            low++;
            high--;
        }


        return cnt;
    }
}