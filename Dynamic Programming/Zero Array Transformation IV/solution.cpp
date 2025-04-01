class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int result = 0;
        for(int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if(!num) continue;
            vector<int> possible(1001);
            possible[num] = 1;
            for(int j = 0; j < queries.size(); ++j) {
                auto& q = queries[j];
                int l = q[0], r = q[1], v = q[2];
                if(i < l || i > r) continue;
                for(int pos = v; pos <= 1000; ++pos) {
                    possible[pos-v] |= possible[pos];
                }
                if(possible[0]) {
                    result = max(result, j+1);
                    break;
                }
            }
            if(!possible[0]) return -1; 
        }
        return result;
    }
};
