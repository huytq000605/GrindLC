class ST {
public:
int n;
vector<int> tree;
    ST(vector<int> &baskets) {
        n = baskets.size();
        tree.resize(4*n);
        for(int i = 0; i < n; ++i) {
            update(i, baskets[i]);
        }
    }
    
    void update(int pos, int v, int i = 0, int l = 0, int r = -1) {
        if(r == -1) r = n-1;
        if(l > pos || r < pos) return;
        if(l == r && pos == l) {
            tree[i] = v;
            return;
        }
        int m = l + (r - l) / 2;
        update(pos, v, i*2+1, l, m);
        update(pos, v, i*2+2, m+1, r);
        tree[i] = max(tree[i*2+1], tree[i*2+2]);
    }
    
    bool place(int v, int i = 0, int l = 0, int r = -1) {
        if(r == -1) r = n-1;
        if(tree[i] < v) return false;
        if(l == r) {
            if(tree[i] >= v) {
                tree[i] = 0;
                return true;
            }
            return false;
        }
        int m = l + (r - l) / 2;
        bool ret = false;
        if(place(v, i * 2 + 1, l, m)) ret = true;
        if(!ret && place(v, i * 2 + 2, m+1, r)) ret = true;
        tree[i] = max(tree[i*2+1], tree[i*2+2]);
        return ret;
    }
};

class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        auto st = ST(baskets);
        int result = 0;
        for(auto f: fruits) {
            if(!st.place(f)) ++result;
        }
        return result;
    }
};
