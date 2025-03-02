class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end());
        int n = pizzas.size() / 4;
        long long result = 0;
        int i = n*4-1, eaten = 0;
        // n/2 pizzas on odd days
        while(eaten < n/2 +(n & 1)) {
            result += pizzas[i];
            --i;
            ++eaten;
        }
        --i;
        // n/2 pizzas on even days
        while(eaten < n) {
            result += pizzas[i];
            i -= 2;
            ++eaten;
        }
        return result;
    }
};
