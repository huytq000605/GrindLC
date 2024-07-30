class BST {
public:
    BST *left = nullptr, *right = nullptr;
    int val = 0, count_left = 0;
    BST(int val = 0, BST *left = nullptr, BST *right = nullptr) : val(val) {}

    void insert(int v) {
        if(v > val) {
            if(right == nullptr) right = new BST(v);
            else right->insert(v);
        } else {
            count_left++;
            if(left == nullptr) left = new BST(v);
            else left->insert(v);
        }
    }

    BST* remove(int v) {
        if (v == val) {
            if(left == nullptr) return right;
            auto right_most = left;
            while(right_most->right != nullptr) {
                right_most = right_most->right;
            }
            right_most->right = right;
            return left;
        } else if(v > val) {
            right = right->remove(v);
        } else {
            left = left->remove(v);
            count_left--;
        }
        return this;
    }

    int count(int v) {
        if(v < val) {
            return left == nullptr ? 0: left->count(v);
        } else {

            return count_left + 1 + (right == nullptr ? 0 : right->count(v));
        }
    } 
};

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        BST *left = new BST(rating.front()), *right = new BST(rating.back());
        int result = 0;
        for(int i = 1; i < n-1; i++) {
            right->insert(rating[i]);        
        }
        for(int j = 1; j < n-1 ; j++) {
            int r = rating[j];
            right->remove(r);
            int left_lt = left->count(rating[j]);
            int right_lt = right->count(rating[j]);
            cout << left_lt << " " << j << " " << right_lt << endl;
            result += left_lt * (n - j - 1 - right_lt) + (j - left_lt) * (right_lt);
            left->insert(r);
        }
        return result;
    }
};
