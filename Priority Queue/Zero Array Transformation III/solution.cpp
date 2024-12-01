class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        sort(queries.begin(), queries.end());
        priority_queue<int> pq;
        int nq = queries.size();
        vector<int> end(nums.size() + 1, 0);
        for(int i{}, iq{}, nq = queries.size(), used{}; i < nums.size(); ++i) {
            while(iq < nq && i >= queries[iq][0]) {
                pq.emplace(queries[iq++][1]);
            }
            
            while(used < nums[i]) {
                if(pq.empty() || pq.top() < i) return -1;
                --end[pq.top()];
                pq.pop();
                ++used;
            }
            used += end[i];
        }
        
        return pq.size();
    }
};
