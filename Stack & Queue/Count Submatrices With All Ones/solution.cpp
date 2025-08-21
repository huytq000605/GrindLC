class Solution {
public:
    int numSubmat(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<int> height(n);
        int result = 0;
        for(int r = 0; r < m; ++r) {
            vector<int> st;
            vector<int> res(n);
            for(int c = 0; c < n; ++c) {
                if(matrix[r][c]) ++height[c];
                else height[c] = 0;
                while(!st.empty() && height[st.back()] >= height[c]) {
                    st.pop_back();
                }
                if(!st.empty()) {
                    int pc = st.back();
                    res[c] = res[pc] + height[c] * (c - pc);
                } else {
                    res[c] = height[c] * (c+1);
                }
                st.push_back(c);
            }
            result += accumulate(res.begin(), res.end(), 0);
        }
        return result;
    }
};
