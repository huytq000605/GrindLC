class Solution {
public:
    int minDays(vector<int>& bloomDay, int m, int k) {
        if(static_cast<long long>(k) * m > bloomDay.size()) return -1;
        auto valid = [&](int days) -> bool {
            int cur = 0;
            int bouquets = 0;
            for(int d: bloomDay) {
                if(d <= days) {
                    cur += 1;
                } else {
                    cur = 0;
                }
                if(cur == k) {
                    bouquets += 1;
                    cur = 0;
                    if(bouquets == m) return true;
                }
            }
            return false;
        };
        int start = 0, end = *max_element(bloomDay.begin(), bloomDay.end());
        while(start < end) {
            int mid = start + (end - start) / 2;
            if(valid(mid)) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
};
