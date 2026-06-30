class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] arrs = new int[26];
        int[] arrt = new int[26];

        for (int i = 0; i < s.length(); i++) {
            if (arrs[s.charAt(i) - 'a'] != arrt[t.charAt(i) - 'a']) return false;

            arrs[s.charAt(i) - 'a'] = i + 1;
            arrt[t.charAt(i) - 'a'] = i + 1;
        }

        return true;
    }
}