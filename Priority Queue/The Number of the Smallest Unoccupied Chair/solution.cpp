class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int target = times[targetFriend][0];
        sort(times.begin(), times.end(), [](auto &t1, auto &t2) -> bool {
            return t1[0] < t2[0];
        });
        priority_queue<int, vector<int>, decltype([](int a, int b) -> bool {
            return a > b;
        })> free;
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype([](auto p1, auto p2) -> bool {
            return p1.first > p2.first;
        })> reserved;
        for(auto &t: times) {
            int u = t[0], v = t[1];
            while(!reserved.empty() && reserved.top().first <= u) {
                auto [_, chair] = reserved.top();
                free.emplace(chair);
                reserved.pop();
            }
            int chair = free.empty() ? reserved.size() : free.top();
            if(!free.empty()) free.pop();
            if(u == target) return chair;
            reserved.emplace(v, chair);
        }
        return -1;
    }
};
