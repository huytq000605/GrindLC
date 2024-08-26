/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        if(root == nullptr) return {};
        vector<int> result;
        stack<Node*> st;
        st.emplace(root);
        while(!st.empty()) {
            auto u = st.top();
            st.pop();
            result.emplace_back(u->val);
            for(auto v = u->children.begin(); v != u->children.end(); v++) {
                st.emplace(*v);
            }
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
