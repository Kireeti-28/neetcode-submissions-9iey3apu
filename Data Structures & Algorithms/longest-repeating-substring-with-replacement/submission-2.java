/*
- find longest window where distinct ele within window is <= k
*/

class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> mp = new HashMap<>();
        int l = 0;

        int ans = 0, maxF = 0;
        for (int r = 0; r < s.length(); r++) {
            mp.put(s.charAt(r), mp.getOrDefault(s.charAt(r), 0) + 1);
            maxF = Math.max(maxF, mp.get(s.charAt(r)));
            while ((r - l + 1) - maxF > k) {
                mp.put(s.charAt(l), mp.get(s.charAt(l)) - 1);
                l++;
            }

            ans = Math.max(ans, r - l + 1);
        }

        return ans;
    }
}
