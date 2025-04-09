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
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        unordered_set<TreeNode*> leafs;
        unordered_map<TreeNode*, TreeNode*> parents;
        deque<TreeNode*> bfs;
        int depth = 0;
        bfs.emplace_back(root);
        int leaf_depth = 0;
        while(!bfs.empty()) {
            int k = bfs.size();
            while(k--) {
                auto u = bfs.front();
                bfs.pop_front();
                if(u->left == nullptr && u->right == nullptr) {
                    if(depth > leaf_depth) {
                        leafs.clear();
                        leaf_depth = depth;
                    }
                    leafs.emplace(u); 
                } else {
                    if(u->left) {
                        parents[u->left] = u;
                        bfs.emplace_back(u->left);
                    }
                    if(u->right) {
                        parents[u->right] = u;
                        bfs.emplace_back(u->right);
                    }
                }
            }
            ++depth;
        }
        while(leafs.size() > 1) {
            unordered_set<TreeNode*> nleafs;
            for(auto u: leafs) {
                nleafs.emplace(parents[u]);
            }
            leafs = nleafs;
        }
        return *leafs.begin();
    }
};
