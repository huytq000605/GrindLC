class Solution {
public:
    int shareCandies(vector<int>& candies, int k) {
        unordered_map<int, int> counter;
        for(int c: candies) ++counter[c];
        int result{};
        for(int i{}, j{}; i < candies.size(); ++i) {
            if(i >= k) ++counter[candies[j++]];
            --counter[candies[i]];
            if(!counter[candies[i]]) counter.erase(candies[i]);
            if(i >= k-1) result = max(result, static_cast<int>(counter.size()));
        }
        return result;
    }
};
