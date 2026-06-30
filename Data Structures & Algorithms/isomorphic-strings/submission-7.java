class Solution {
    public boolean isIsomorphic(String s, String t) {
        // Use 256 to support all ASCII characters safely
        int[] mapS = new int[256];
        int[] mapT = new int[256];
        
        for (int i = 0; i < s.length(); i++) {
            char charS = s.charAt(i);
            char charT = t.charAt(i);
            
            // If their last seen positions don't match, they aren't isomorphic
            if (mapS[charS] != mapT[charT]) {
                return false;
            }
            
            // Store i + 1 (so 0-index is distinct from default 0 array value)
            mapS[charS] = i + 1;
            mapT[charT] = i + 1;
        }
        
        return true;
    }
}