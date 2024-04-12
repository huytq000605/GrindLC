class Solution {
public:
    int trap(vector<int>& height) {
        int result = 0;
        stack<int> st;
        for(int i = 0; i < height.size(); i++) {
            while(st.size() && height[i] >= height[st.top()]) {
                int btm = height[st.top()];
                st.pop();
                if(!st.size()) break;
                int j = st.top();
                int width = i - j - 1;
                result += (min(height[j], height[i]) - btm) * width;
            }
            st.push(i);
        }
        return result;
    }
};
