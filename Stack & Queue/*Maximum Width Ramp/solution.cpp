class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        int result = 0;
        stack<int> st;
        for(int i = 0; i < nums.size(); ++i) if(st.empty() || nums[i] < nums[st.top()]) st.emplace(i);
        for(int i = nums.size()-1; i >= 0 && !st.empty(); --i) {
            while(!st.empty() && nums[i] >= nums[st.top()]) {
                result = max(result, i - st.top());
                st.pop();
            }
        }
        return result;
    }
};
