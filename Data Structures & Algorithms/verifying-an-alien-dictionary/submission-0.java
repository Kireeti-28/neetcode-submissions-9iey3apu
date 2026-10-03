class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> orderMap = new HashMap<>();

        for (int i = 0; i < order.length(); i++) {
            orderMap.put(order.charAt(i), i);
        }

        for (int i = 0; i < words.length - 1; i++) {
            String word1 = words[i];
            String word2 = words[i + 1];

            for (int j = 0; j < word1.length(); j++) {
                if (j == word2.length()) return false;
                if (word1.charAt(j) != word2.charAt(j)) {
                    if (orderMap.get(word1.charAt(j)) > orderMap.get(word2.charAt(j))) {
                        return false;
                    }
                    break;
                }
            }
        }

        return true;
    }
}