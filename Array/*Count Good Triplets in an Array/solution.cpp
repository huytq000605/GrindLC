class ST {
public:
    vector<int> tree;
    int n;
    ST(int _n): n(_n) {
        tree.resize(4*n);
    }

    long long query(int s, int e, int i = 0, int l = 0, int r = -1) {
        if(r == -1) r = n-1;
        // cout << s << " " << e << " " << i << " " << l << " " << r << endl;
        if(s > r || e < l) {
            return 0;
        }
        if(s <= l && e >= r) {
            return tree[i];
        }
        int m = l + (r-l)/2;
        return query(s, e, i*2+1, l, m) + query(s, e, i*2+2, m+1, r);
    }

    void set(int p, int i = 0, int l = 0, int r = -1) {
        if(r == -1) r = n-1;
        if(p < l || p > r) return;
        if(l == r && l == p) {
            tree[i] = 1;
            return;
        }
        int m = l + (r-l)/2;
        set(p, i*2+1, l, m);
        set(p, i*2+2, m+1, r);
        tree[i] = tree[i*2+1] + tree[i*2+2];
    }
};

class Solution {
public:
    long long goodTriplets(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size();
        vector<int> idxs(n);
        for(int i = 0; i < n; ++i) {
            idxs[nums2[i]] = i;
        }
        for(int i = 0; i < n; ++i) {
            nums1[i] = idxs[nums1[i]];
        }
        auto st = ST(n);
        long long result = 0;
        for(int i = 0; i < n; ++i) {
            int j = nums1[i];
            long long left = st.query(0, j);
            long long right = (n-(j+1)) - (i-left); // num of greater index - (num of invalid greater index)
            result += left * right;
            st.set(j);
        }
        return result;
    }
};
