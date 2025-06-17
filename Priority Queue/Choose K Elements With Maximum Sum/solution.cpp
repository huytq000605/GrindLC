class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<pair<int, int>> inums1(n);
        for(int i = 0; i < n; ++i) {
            inums1[i] = {i, nums1[i]};
        }
        sort(inums1.begin(), inums1.end(), [](auto &p1, auto &p2) {
            return p1.second < p2.second;
        });
        priority_queue<int, vector<int>, greater<int>> pq;
        long long s = 0;
        vector<long long> result(n);
        
        int j = 0;
        for(auto [i, num]: inums1) {
            while(inums1[j].second < num) {
                int idx = inums1[j].first;
                s += nums2[idx];
                pq.emplace(nums2[idx]);
                if(pq.size() > k) {
                    s -= pq.top(); pq.pop();
                }
                ++j;
            }
            result[i] = s;
            
        }
        return result;
        
    }
};
