class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        vector<int> result(prices.begin(), prices.end());
        vector<int> st; 
        for(int i{}; i < prices.size(); ++i) {
            while(!st.empty() && prices[st.back()] >= prices[i]) {
                result[st.back()] -= prices[i];
                st.pop_back();
            }
            st.emplace_back(i);
        }
        return result;
    }
};
