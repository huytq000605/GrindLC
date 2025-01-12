class SegmentTree {
struct Node {
    long long total_sum, prefix_sum, suffix_sum, max_sum;
};
vector<Node> tree;
int n;

public:
    SegmentTree(int _n): n(_n) {
        tree.resize(4 * n);
    }

    Node query(int start, int end, int l = 0, int r = -1, int i = 0) {
        if(r == -1) r = n-1;
        if(start <= l && end >= r) return tree[i];
        if(start > r || end < l) return {0, LLONG_MIN, LLONG_MIN, LLONG_MIN};
        int mid = l + (r - l) / 2;
        Node left = query(start, end, l, mid, i*2+1);
        Node right = query(start, end, mid+1, r, i*2+2);
        Node result;
        result.prefix_sum = max(left.total_sum + right.prefix_sum, left.prefix_sum);
        result.suffix_sum = max(left.suffix_sum + right.total_sum, right.suffix_sum);
        result.total_sum = left.total_sum + right.total_sum;
        result.max_sum = max({left.max_sum, right.max_sum, left.suffix_sum + right.prefix_sum});
        return result;
    }

    void update(int start, int end, long long val, int l = 0, int r = -1, int i = 0) {
        if(r == -1) r = n-1;
        if(start <= l && end >= r) {
            tree[i] = {val, val, val, val};
            return;
        }
        if(start > r || end < l) return;
        int mid = l + (r - l) / 2;
        update(start, end, val, l, mid, i*2+1);
        update(start, end, val, mid+1, r, i*2+2);
        Node left = tree[i*2+1];
        Node right = tree[i*2+2];
        tree[i].prefix_sum = max(left.total_sum + right.prefix_sum, left.prefix_sum);
        tree[i].suffix_sum = max(left.suffix_sum + right.total_sum, right.suffix_sum);
        tree[i].total_sum = left.total_sum + right.total_sum;
        tree[i].max_sum = max({left.max_sum, right.max_sum, left.suffix_sum + right.prefix_sum});
    }

    Node build(vector<int> &nums, int l = 0, int r = -1, int i = 0) {
        if(r == -1) r = n-1;
        if(l == r) {
            tree[i] = {nums[l], nums[l], nums[l], nums[l]};
            return tree[i];
        } else {
            int mid = l + (r - l) / 2;
            Node left = build(nums, l, mid, i*2+1);
            Node right = build(nums, mid+1, r, i*2+2);
            tree[i].prefix_sum = max(left.total_sum + right.prefix_sum, left.prefix_sum);
            tree[i].suffix_sum = max(left.suffix_sum + right.total_sum, right.suffix_sum);
            tree[i].total_sum = left.total_sum + right.total_sum;
            tree[i].max_sum = max({left.max_sum, right.max_sum, left.suffix_sum + right.prefix_sum});
            return tree[i];
        }
    }
};



class Solution {
public:
    long long maxSubarraySum(vector<int>& nums) {
        // special scenarios when all nums are negative
        int mx = *max_element(nums.begin(), nums.end());
        if(mx <= 0) return mx;

        unordered_map<int, vector<int>> value_idxs;
        for(int i{}; i < nums.size(); ++i) {
            value_idxs[nums[i]].emplace_back(i);
        }

        int n = nums.size();
        SegmentTree st(n);
        st.build(nums);
        long long result = st.query(0, n-1).max_sum;

        for(auto &[v, idxs]: value_idxs) {
            for(int i: idxs) {
                st.update(i, i, 0);
            }
            auto q = st.query(0, n-1);
            result = max(result, q.max_sum);
            for(int i: idxs) {
                st.update(i, i, v);
            }
        }
        return result;

    }
};
