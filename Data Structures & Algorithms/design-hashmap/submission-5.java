class MyHashMap {
    private int[] bucket;
    private static final int MAX = 1000001;

    public MyHashMap() {
        this.bucket = new int[MAX];
        Arrays.fill(this.bucket, -1);
    }
    
    private int hash(int key) {
        return (key % MAX);
    }

    public void put(int key, int value) {
        int idx = hash(key);
        this.bucket[idx] = value;
    }
    
    public int get(int key) {
        int idx = hash(key);
        return this.bucket[idx];
    }
    
    public void remove(int key) {
        int idx = hash(key);
        this.bucket[idx] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */