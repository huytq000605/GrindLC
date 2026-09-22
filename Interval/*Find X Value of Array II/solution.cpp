class ST {
public:
int n, k;
vector<pair<int, array<int, 5>>> tree;
    ST(vector<int>& nums, int _k) {
        n = nums.size();
        k = _k;
        tree.resize(4*n);
        build(nums);
    }   
    pair<int, array<int, 5>> query(int l, int r, int i = 0, int tl = 0, int tr = -1) {
        if(tr == -1) tr = n-1;
        if(r < tl || l > tr) return {1, array<int, 5>{}};
        if(l <= tl && r >= tr) return tree[i];
        int tm = tl + (tr - tl) / 2;
        auto left = query(l, r, i*2+1, tl, tm);
        auto right = query(l, r, i*2+2, tm+1, tr);
        return merge(left, right);
    }

    pair<int, array<int, 5>> merge(pair<int, array<int, 5>>& left, pair<int, array<int, 5>>& right) {
        array<int, 5> freq(left.second);
        for(int j = 0; j < k; ++j) {
            // must use prefix as suffix will fuck up the non-static "start"
            if(right.second[j]) {
                int p = left.first * j % k;
                freq[p] += right.second[j];
            } 
        }
        return {left.first * right.first % k, freq};
    }

    void build(vector<int>& nums, int i = 0, int tl = 0, int tr = -1) {
        if(tr == -1) tr = n-1;
        if(tl == tr) {
            array<int, 5> ms{};
            ms[nums[tl]%k] = 1;
            tree[i] = {nums[tl]%k, ms};
            return;
        }
        int tm = tl + (tr - tl) / 2;
        build(nums, i*2+1, tl, tm);
        build(nums, i*2+2, tm+1, tr);
        tree[i] = merge(tree[i*2+1], tree[i*2+2]);
    }

    void update(int ui, int uv, int i = 0, int tl = 0, int tr = -1) {
        if(tr == -1) tr = n-1;
        if(ui < tl || ui > tr) return;
        if(tl == tr) {
            array<int, 5> ms{};
            ms[uv%k] = 1;
            tree[i] = {uv % k, ms};
            return;
        }
        
        int tm = tl + (tr - tl) / 2;
        update(ui, uv, i*2+1, tl, tm);
        update(ui, uv, i*2+2, tm+1, tr);
        tree[i] = merge(tree[i*2+1], tree[i*2+2]);
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        auto st = ST(nums, k);
        vector<int> result(queries.size());
        for(int iq = 0; iq < queries.size(); iq++) {
            auto &q = queries[iq];
            int i = q[0], v = q[1], s = q[2], x = q[3];
            st.update(i, v);
            result[iq] = st.query(s, n-1).second[x];
        }
        return result;     
    }
};
