class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int mx = *max_element(begin(costs), end(costs));
        vector<int> counter(mx+1);
        for(int cost: costs) counter[cost] += 1;
        int result = 0;
        for(int cost = 1; cost < counter.size() && coins >= cost; ++cost) {
            int m = min(coins / cost, counter[cost]);
            result += m;
            coins -= m * cost;
        }
        return result;
    }
};
