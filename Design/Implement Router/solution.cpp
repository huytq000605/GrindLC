class Router {
    int limit;
    deque<tuple<int, int, int>> pkgs;
    unordered_map<int, deque<int>> bydes;
    set<pair<int, int>> dedup;
    int t = 0;
public:
    Router(int memoryLimit) {
        limit = memoryLimit;
    }
    
    bool addPacket(int source, int destination, int timestamp) {
        if(timestamp > t) dedup.clear();
        if(dedup.find({source, destination}) != dedup.end()) return false;
        if(pkgs.size() == limit) {
            auto [src, des, time] = pkgs.front();
            bydes[des].pop_front();
            pkgs.pop_front();
            if(time == t) dedup.erase({src, des});
        }
        pkgs.emplace_back(source, destination, timestamp);
        bydes[destination].emplace_back(timestamp);
        dedup.emplace(source, destination);
        t = timestamp;
        return true;
    }
    
    vector<int> forwardPacket() {
        if(pkgs.empty()) return {};
        auto [src, des, time] = pkgs.front(); pkgs.pop_front();
        bydes[des].pop_front();
        if(time == t) dedup.erase({src, des});
        return {src, des, time};
    }
    
    int getCount(int destination, int startTime, int endTime) {
        auto &a = bydes[destination];
        return lower_bound(a.begin(), a.end(), endTime+1) - lower_bound(a.begin(), a.end(), startTime);
    }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */
