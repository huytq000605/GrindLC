class Solution {
public:
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.rbegin(), workers.rend());
        auto valid = [&](int k) {
            multiset<int> sworkers = multiset(workers.begin(), workers.begin() + k);
            int pills_used = 0;
            for(int t = k-1, w = 0; t >= 0; --t, ++w) {
                if(*prev(sworkers.end()) < tasks[t]) {
                    if(pills_used == pills || *prev(sworkers.end()) + strength < tasks[t]) 
                        return false;
                    sworkers.erase(sworkers.lower_bound(tasks[t] - strength));
                    ++pills_used;
                } else {
                    sworkers.erase(prev(sworkers.end()));
                }
            }
            return true;
        };
        int lo = 0, hi = min(workers.size(), tasks.size());
        while(lo < hi) {
            int mi = lo + (hi - lo + 1) / 2;
            if(valid(mi)) {
                lo = mi;
            } else {
                hi = mi - 1;
            }
        }
        return lo;
    }
};
