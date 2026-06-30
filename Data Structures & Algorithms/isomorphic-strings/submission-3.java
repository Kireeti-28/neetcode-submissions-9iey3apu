class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] arrs = new int[26];
        int[] arrt = new int[26];

        for (int i = 0; i < s.length(); i++) {
            System.out.println(Arrays.toString(arrs));
            if (arrs[s.charAt(i) - 'a'] != arrt[t.charAt(i) - 'a']) return false;

            arrs[s.charAt(i) - 'a']++;
            arrt[t.charAt(i) - 'a']++;
        }

        return true;
    }
}