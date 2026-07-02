class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> mp = new HashMap();

        for (int i = 0; i < s.length(); i++) {
            mp.put(s.charAt(i), mp.getOrDefault(s.charAt(i), 0) + 1);
        }

        for (int j = 0; j < t.length(); j++) {
            mp.put(t.charAt(j), mp.getOrDefault(t.charAt(j), 0) - 1);

            if (mp.get(t.charAt(j)) == -1) return false;
        }

        for (Map.Entry<Character, Integer> entry: mp.entrySet()) {
            if (entry.getValue() != 0) return false;
        }

        return true;
    }
}
