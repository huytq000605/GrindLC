class Solution {
public:
    int minimumCost(vector<int>& cost) {
        sort(rbegin(cost), rend(cost));
        int result = 0;
        for(int i = 0; i < cost.size(); ++i) {
            if((i+1) % 3 == 0) continue;
            result += cost[i];
        }
        return result;
    }
};
