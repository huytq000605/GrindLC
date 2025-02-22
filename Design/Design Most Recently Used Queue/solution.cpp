class MRUQueue {
vector<deque<int>> buckets;
int sq;
public:
    MRUQueue(int n) {
        sq = ceil(sqrt(n));
        buckets.resize(sq);
        for(int i{}; i < n; ++i) {
            buckets[i/sq].emplace_back(i+1);
        }
        if(buckets.back().empty()) buckets.pop_back();
    }
    
    int fetch(int k) {
        k -= 1;
        int bucket = k / sq;
        int idx = k % sq;
        int target = buckets[bucket][idx];
        for(int i{idx}; i < buckets[bucket].size() - 1; ++i) {
            buckets[bucket][i] = buckets[bucket][i+1];
        }
        buckets[bucket].pop_back();
        for(int i{bucket}; i < buckets.size()-1; ++i) {
            buckets[i].emplace_back(buckets[i+1].front());
            buckets[i+1].pop_front();
        }
        buckets.back().emplace_back(target);
        return target;
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */
