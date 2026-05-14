class Solution {
public:
    int minimumEffort(vector<vector<int>>& tasks) {
        sort(begin(tasks), end(tasks), [](auto& t1, auto &t2) -> bool { 
            int d1 = t1[1] - t1[0];
            int d2 = t2[1] - t2[0];
            return d1 > d2; 
        });
        int result = 0;
        int remaining = 0;
        for(auto &t: tasks) {
            if(remaining < t[1]) {
                int d = t[1] - remaining;
                result += d;
                remaining += d;
            }
            remaining -= t[0];
        }
        return result;
    }
};
