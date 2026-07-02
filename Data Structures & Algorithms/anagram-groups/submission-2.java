class Solution {
    public String getKey(String str) {
        int[] arr = new int[26];

        for (char s: str.toCharArray()) {
            arr[s - 'a'] += 1;
        }

        return Arrays.toString(arr);
    }
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mp = new HashMap();

        for (String str: strs) {
            String key = getKey(str);
            var val = mp.getOrDefault(key, new ArrayList());
            val.add(str);
            mp.put(key, val);
        }

        List<List<String>> ans = new ArrayList();
        for (Map.Entry<String, List<String>> entry: mp.entrySet()) {
            ans.add(entry.getValue());
        }
        
        return ans;
    }
}
