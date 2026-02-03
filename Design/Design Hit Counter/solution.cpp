class HitCounter {
    deque<pair<int, int>> dq;
    int counter = 0;
public:
    HitCounter() {
    }
    void hit(int timestamp) {
        if(!dq.empty() && dq.back().first == timestamp) {
            dq.back().second += 1;
        } else {
            dq.emplace_back(timestamp, 1);
        }
        ++counter;
    }
    
    int getHits(int timestamp) {
        while(!dq.empty() && dq.front().first + 300 <= timestamp) {
            counter -= dq.front().second;
            dq.pop_front();
        }
        return counter;
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */
