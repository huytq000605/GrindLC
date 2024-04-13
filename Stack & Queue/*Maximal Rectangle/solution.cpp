class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int result = 0;
        // Set the height of virtual latest column to be always 0
        vector<int> heights(n + 1, 0);
        for(int r = 0; r < m; r++) {
            for(int c = 0; c < n; c++) {
                if(matrix[r][c] == '1') {
                    heights[c] += 1;
                } else {
                    heights[c] = 0;
                }
            }

            stack<int> st;
            for(int c = 0; c < n + 1; c++) {
                while(st.size() && heights[c] < heights[st.top()]) {
                    int h = heights[st.top()];
                    st.pop();
                    int w = st.size() ? c - 1 - st.top() : c;
                    result = max(result, w * h);
                }
                st.push(c);
            }
        }
        return result;
    }
};
