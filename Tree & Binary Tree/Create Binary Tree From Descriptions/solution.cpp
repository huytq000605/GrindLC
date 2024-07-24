/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> values;
        unordered_map<int, int> ind;
        for(auto node: descriptions) {
            int parent = node[0], child = node[1], is_left = node[2];
            for(auto u: vector<int>{parent, child}) {
                if(values.find(u) == values.end()) {
                    values[u] = new TreeNode(u);
                    ind[u] = 0;
                }
            }
            ind[child] += 1;
            TreeNode *u = values[parent], *v = values[child];
            if(is_left) {
                u->left = v;
            } else {
                u->right = v;
            }
        }

        for(auto it: ind) {
            if(!it.second) return values[it.first];
        }
        return NULL;
    }
};
