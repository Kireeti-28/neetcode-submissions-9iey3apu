class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> mp = new HashMap();
        int l = 0;
        int r = 0;
        int n = s.length();
        int ans = 0;

        while (r < n) {
            mp.put(s.charAt(r), mp.getOrDefault(s.charAt(r), 0) + 1);

            while (mp.get(s.charAt(r)) > 1) {
                mp.put(s.charAt(l), mp.get(s.charAt(l)) - 1);
                if (mp.get(s.charAt(l)) == 0)
                    mp.remove(s.charAt(l));
                l++;
            }

            ans = Math.max(mp.size(), ans);
            r++;
        }

        return ans;
    }
}
