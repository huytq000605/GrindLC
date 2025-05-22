class Solution {
public:
    int maxRemoval(vector<int>& nums, vector<vector<int>>& queries) {
        sort(queries.begin(), queries.end());
        priority_queue<int> pq;
        int nq = queries.size();
        vector<int> end(nums.size(), 0);
        int in_use = 0;
        for(int i = 0, iq = 0; i < nums.size(); ++i) {
            while(iq < nq && queries[iq][0] <= i) {
                pq.emplace(queries[iq++][1]);
            }
            while(in_use < nums[i]) {
                if(pq.empty() || pq.top() < i) return -1;
                ++in_use;
                --end[pq.top()]; pq.pop();
            }
            in_use += end[i];
        }
        return pq.size();
    }
};
