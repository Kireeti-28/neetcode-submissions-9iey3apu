class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> mp = new HashMap();
        int l = 0;
        int r = 0;
        int maxFreq = 0;
        int ans = 0;

        while (r < s.length()) {
            mp.put(s.charAt(r), mp.getOrDefault(s.charAt(r), 0) + 1);
            maxFreq = Math.max(maxFreq, mp.get(s.charAt(r)));
            while ((r - l + 1) - maxFreq > k) {
                mp.put(s.charAt(l), mp.get(s.charAt(l)) - 1);
                if (s.charAt(l) == 0) mp.remove(s.charAt(l));

                l++;
            }

            ans = Math.max(ans, (r - l + 1));
            r++;
        }

        return ans;
    }
}
