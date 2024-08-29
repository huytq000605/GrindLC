class Solution {
public:
    int pathSum(vector<int>& nums) {
        vector<array<int, 8>> depths(4, array<int, 8>{-1, -1, -1, -1, -1, -1, -1, -1});
        for(int num: nums) {
            int d = num / 100 - 1;
            int p = (num % 100) / 10 - 1;
            int v = num % 10;
            depths[d][p] = v;
        }
        int result = 0;
        int d = 0;
        deque<pair<int, int>> dq;
        dq.emplace_back(0, depths[0][0]);
        while(!dq.empty()) {
            deque<pair<int, int>> ndq;
            while(!dq.empty()) {
                auto [u, s] = dq.front();
                dq.pop_front();
                bool is_leaf = true;
                if(d+1 < depths.size()) {
                    if(depths[d+1][u*2] != -1) {
                        ndq.emplace_back(u*2, s + depths[d+1][u*2]);
                        is_leaf = false;
                    }
                    if(depths[d+1][u*2+1] != -1) {
                        ndq.emplace_back(u*2+1, s + depths[d+1][u*2+1]);
                        is_leaf = false;
                    }
                }
                if(is_leaf) result += s;
            }
            swap(ndq, dq);
            d++;
        }
        return result;
    }
};
