class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        auto cmp = [](auto p1, auto p2) -> bool {
            if(p1.second == p2.second) {
                return p1.first < p2.first;
            }
            return p1.second < p2.second;
        };
        set<pair<int, int>, decltype(cmp)> top;
        set<pair<int, int>, decltype(cmp)> btm;
        map<int, int> counter;
        vector<long long> result;
        long long s = 0;
        for(int i = 0; i < nums.size(); ++i) {
            if(i >= k) {
                long long num = static_cast<long long>(nums[i-k]);
                if(top.erase({num, counter[num]})) s-= num * counter[num];
                btm.erase({num, counter[num]});
                --counter[num];
                if(!counter[num]) counter.erase(num);
                else btm.emplace(num, counter[num]);
                while(top.size() < x && !btm.empty()) {
                    auto [num, freq] = *btm.rbegin();
                    btm.erase(--btm.end());
                    s += static_cast<long long>(num) * freq;
                    top.emplace(num, freq);
                }
            }

            long long num = static_cast<long long>(nums[i]);
            if(top.erase({num, counter[num]})) s -= num * counter[num];
            btm.erase({num, counter[num]});
            ++counter[num];
            top.emplace(num, counter[num]);
            s += num * counter[num];
            if(top.size() > x) {
                auto [num, freq] = *top.begin();
                top.erase(top.begin());
                s -= static_cast<long long>(num) * freq;
                btm.emplace(num, freq);
            }
            if(i >= k-1) {
                result.emplace_back(s);
            }
        }
        return result;
    }
};
