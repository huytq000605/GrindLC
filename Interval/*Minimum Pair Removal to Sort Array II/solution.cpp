class Solution {
public:
    int minimumPairRemoval(vector<int>& A) {
        int n = A.size();
        vector<long long> nums(n);
        for(int i = 0; i < n; ++i) {
            nums[i] = A[i];
        }
        
        set<pair<long long, int>> pairs;
        vector<int> next(n, n), prev(n, -1);
        int count = 0;
        for(int i = 0; i < n-1; ++i) {
            if(nums[i] > nums[i+1]) {
                ++count;
            }
            next[i] = i+1;
            prev[i] = i-1;
            pairs.emplace(nums[i] + nums[i+1], i);
        }
        int result = 0;
        while(count) {
            ++result;
            auto [s, i] = *pairs.begin();
            int j = next[i];
            int p = prev[i], q = next[j];
            if(nums[i] > nums[j]) --count;
            if(p >= 0 && nums[p] > nums[i]) --count;
            if(q < n && nums[j] > nums[q]) --count;

            pairs.erase({s, i});
            if(q < n) pairs.erase({nums[j] + nums[q], j});
            if(p >= 0) pairs.erase({nums[p] + nums[i], p});
        
            nums[i] += nums[j];
            if(p >= 0) {
                pairs.emplace(nums[p] + nums[i], p);
                if(nums[p] > nums[i]) ++count;
            }
            if(q < n) {
                pairs.emplace(nums[i] + nums[q], i);
                if(nums[i] > nums[q]) ++count;
            }
            
            next[i] = q;
            if(q < n) prev[q] = i;
        }
        return result;
    }
};
