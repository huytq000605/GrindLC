/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/

class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if(root == nullptr) return nullptr;
        Node* ret = nullptr;
        Node* prev = nullptr;
        auto dfs = [&ret, &prev](this auto&& dfs, Node* node) -> void {
            if(node == nullptr) return;
            dfs(node->left);
            if(prev) {
                node->left = prev;
                prev->right = node;
            } else {
                ret = node;
            }
            prev = node;
            dfs(node->right);
        };
        dfs(root);
        ret->left = prev;
        prev->right = ret;
        return ret;
    }
};
