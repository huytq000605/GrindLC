class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        int limit = INT_MIN;
        stack<int> st;
        for(auto & p: preorder) {
            if(p < limit) return false;
            while(st.size() > 0 && p > st.top()) {
                limit = st.top();
                st.pop();
            }
            st.push(p);
        }
        return true;
    }
};
