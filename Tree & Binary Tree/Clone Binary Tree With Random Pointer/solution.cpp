/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     Node *left;
 *     Node *right;
 *     Node *random;
 *     Node() : val(0), left(nullptr), right(nullptr), random(nullptr) {}
 *     Node(int x) : val(x), left(nullptr), right(nullptr), random(nullptr) {}
 *     Node(int x, Node *left, Node *right, Node *random) : val(x), left(left), right(right), random(random) {}
 * };
 */

class Solution {
public:
    NodeCopy* copyRandomBinaryTree(Node* root) {
        if(!root) return nullptr;
        unordered_map<Node*, NodeCopy*> um;
        deque<Node*> dq{root};
        while(!dq.empty()) {
            auto u = dq.front(); dq.pop_front();
            if(um.find(u) == um.end()) um[u] = new NodeCopy(u->val);
            auto uu = um[u];
            for(auto v: {u->left, u->right, u->random}) {
                if(v == nullptr) continue;
                NodeCopy* vv;
                if(um.find(v) == um.end()) {
                    vv = new NodeCopy(v->val);
                    um[v] = vv;
                } else {
                    vv = um[v];
                }

                if(v == u->left) {
                    uu->left = vv;
                    dq.push_back(v);
                } else if(v == u->right) {
                    uu->right = vv;
                    dq.push_back(v);
                }
                if(v == u->random) uu->random = vv;
            }
        }
        return um[root];
    }
};
