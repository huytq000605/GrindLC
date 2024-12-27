class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& values) {
        int result{};
        for(int i{}, j{1}; j < values.size(); ++j) {
            result = max(result, values[i] + values[j] + i - j);
            if(values[j] + j >= values[i] + i) i = j;
        }
        return result;
    }
};
