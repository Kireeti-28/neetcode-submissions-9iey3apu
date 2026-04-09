class Solution {
    public int findJudge(int n, int[][] trust) {
        Map<Integer, Integer> inFreqMap = new HashMap();
        Map<Integer, Integer> outFreqMap = new HashMap();

        for (int[] trustItem : trust) {
            int in = trustItem[0];
            int out = trustItem[1];

            inFreqMap.put(in, inFreqMap.getOrDefault(in, 0) + 1);
            outFreqMap.put(out, outFreqMap.getOrDefault(out, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entrySet: outFreqMap.entrySet()) {
            if (entrySet.getValue() == trust.length && !inFreqMap.containsKey(entrySet.getKey())) {
                return entrySet.getKey();
            }
        }

        return -1;
    }
}