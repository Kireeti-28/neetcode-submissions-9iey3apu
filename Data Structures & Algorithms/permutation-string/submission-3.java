class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s2.length() < s1.length()) return false;

        int score1 = 0;
        for (char c1: s1.toCharArray()) {
            score1 += c1 - 'a';
        }

        // System.out.println(score1);

        Map<Character, Integer> mp = new HashMap();
        int l = 0;
        int r;
        int score2 = 0;
        for (r = 0; r < s1.length() - 1; r++) {
            mp.put(s2.charAt(r), mp.getOrDefault(s2.charAt(r), 0) + 1);
            score2 += s2.charAt(r) - 'a';
        }

        // System.out.println(score2);

        while (r < s2.length()) {
            mp.put(s2.charAt(r), mp.getOrDefault(s2.charAt(r), 0) + 1);
            score2 += s2.charAt(r) - 'a';
            r++;

            if (score1 == score2) return true;

            mp.put(s2.charAt(l), mp.get(s2.charAt(l)) - 1);
            if (mp.get(s2.charAt(l)) == 0) mp.remove(s2.charAt(l));
            score2 -= s2.charAt(l) - 'a';
            l++;
        }


        return false;
    }
}
