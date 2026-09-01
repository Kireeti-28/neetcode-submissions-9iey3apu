class MyHashSet {
    private int[] bucket;
    private int CAP = 100000;

    public MyHashSet() {
        this.bucket = new int[CAP];
        Arrays.fill(bucket, -1);
    }

    private int hash(int key) {
        return key % CAP;
    }
    
    public void add(int key) {
        int idx = hash(key);
        bucket[idx] = key;
    }
    
    public void remove(int key) {
        int idx = hash(key);
        if (bucket[idx] != -1) {
            bucket[idx] = -1;
        }
    }
    
    public boolean contains(int key) {
        int idx = hash(key);
        return bucket[idx] != -1;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */