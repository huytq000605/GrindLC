class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        int limit = INT_MIN;
        int i = -1;
        for(auto & p: preorder) {
            if(p < limit) return false;
            while(i >= 0 && p > preorder[i]) {
                limit = preorder[i];
                i -= 1;
            }
            preorder[++i] = p;
        }
        return true;
    }
};
