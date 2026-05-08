vector<bool> is_prime(1e6+1, true);
bool init = false;

class Solution {
public:
    int minJumps(vector<int>& nums) {
        if(!init) {
            is_prime[0] = false;
            is_prime[1] = false;
            for(int num = 2; num <= 1e6; ++num) {
                if(is_prime[num]) {
                    for(int nnum = num + num; nnum <= 1e6; nnum += num) {
                        is_prime[nnum] = false;
                    } 
                }
            }
            init = true;
        }
        int mx = *max_element(begin(nums), end(nums));
        int n = nums.size();
        vector<int> dp(n, INT_MAX);
        dp[0] = 0;
        deque<int> dq;
        dq.emplace_back(0);

        unordered_map<int, vector<int>> um;
        for(int i = 0; i < nums.size(); ++i) {
            um[nums[i]].push_back(i);
        }
        while(!dq.empty()) {
            int i = dq.front(); dq.pop_front();
            int s = dp[i];
            if(i == n-1) return s;
            for(int di: {-1, 1}) {
                int ni = i + di;
                if(ni >= 0 && ni < n && s + 1 < dp[ni]) {
                    dp[ni] = s+1;
                    dq.emplace_back(ni);
                }
            }
            if(is_prime[nums[i]]) {
                for(int nnum = nums[i]; nnum <= mx; nnum += nums[i]) {
                    if(um.find(nnum) == um.end()) continue;
                    for(int ni: um[nnum]) {
                        if(s + 1 < dp[ni]) {
                            dp[ni] = s+1;
                            dq.push_back(ni);
                        }
                    }
                    um.erase(nnum);
                }
            }
        }

        return -1;
    }
};
