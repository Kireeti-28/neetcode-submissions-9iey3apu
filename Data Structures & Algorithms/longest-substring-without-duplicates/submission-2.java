class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> mp = new HashMap();
        int l = 0;
        int r = 0;
        int n = s.length();
        int ans = 0;

        while (r < n) {
            char curChar = s.charAt(r);
            int curFreq = mp.getOrDefault(curChar, 0);

            if (curFreq == 0) {
                mp.put(curChar, curFreq + 1);
            } else {
                int newCurFreq = curFreq - 1;
                mp.remove(s.charAt(l));
                l++;
            }

            ans = Math.max(mp.size(), ans);
            r++;
        }

        return ans;
    }
}
