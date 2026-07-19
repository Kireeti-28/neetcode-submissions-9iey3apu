class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> mp = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            mp.put(nums[i], mp.getOrDefault(nums[i], 0) + 1);
        }

        Integer[] arr = Arrays.stream(nums).boxed().toArray(Integer[]::new);

        Arrays.sort(arr, (a, b) -> {
            int freqA = mp.get(a);
            int freqB = mp.get(b);

            if (freqA != freqB) {
                return Integer.compare(freqA,freqB);
            }

            return Integer.compare(b, a);
        });

        return Arrays.stream(arr).mapToInt(a -> a).toArray();
    }
}