class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) return strs[0];

        StringBuilder sb = new StringBuilder();
        String have = strs[0];

        for (int i = 0; i < have.length(); i++) {
            for (int j = 1; j < strs.length; j++) {
                if (i >= strs[j].length() || have.charAt(i) != strs[j].charAt(i)) {
                    return sb.toString();
                }
            }
            sb.append(have.charAt(i));
        }

        return sb.toString();
        
    }
}