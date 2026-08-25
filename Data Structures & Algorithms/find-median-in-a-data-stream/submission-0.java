class MedianFinder {
    private List<Integer> nums;
    public MedianFinder() {
        this.nums = new ArrayList<>();
    }
    public void addNum(int num) {
        this.nums.add(num);
    }
    public double findMedian() {
        if (this.nums.size() == 0) return 0.0;
        List<Integer> sortedNums = this.nums.stream().sorted().toList();
        int n = sortedNums.size() / 2;
        if (this.nums.size() % 2 == 0) {
            // median for even length
            int x1 = sortedNums.get(n - 1);
            int x2 = sortedNums.get(n);
            return (x1 + x2) / 2.0;
        } else {
            // median for odd length
            return (double) sortedNums.get(n);
        }
    }
}
