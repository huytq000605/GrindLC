class Solution {
public:
    vector<int> maximumLengthOfRanges(vector<int>& nums) {
        vector<int> st;
        vector<int> result(nums.size());
        for(int i{}; i < nums.size(); ++i) {
            while(!st.empty() && nums[st.back()] < nums[i]) {
                int j = st.back();
                st.pop_back();
                result[j] = i - (st.empty() ? 0: st.back() + 1);
            }
            st.emplace_back(i);
        }
        while(!st.empty()) {
            int j = st.back();
            st.pop_back();
            result[j] = nums.size() - (st.empty() ? 0: st.back() + 1);
        }
        return result;
    }
};
