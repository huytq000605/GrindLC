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
    Node* cloneTree(Node* root) {
        if(!root) return nullptr;
        auto result = new Node(root->val);
        deque<pair<Node*, Node*>> dq{{root, result}};
        while(!dq.empty()) {
            auto [u, uu] = dq.front(); dq.pop_front();
            for(auto v: u->children) {
                auto vv = new Node(v->val);
                uu->children.push_back(vv);
                dq.emplace_back(v, vv);
            }
        }
        return result;
    }
};
