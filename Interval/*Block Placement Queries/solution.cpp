
class SegmentTree {
public:
    SegmentTree(int _n) {
        n = _n;
        tree.resize(n * 4, 0);
    }

    int query_max(int x) {
        return query_internal(0, x, 0, 0, n-1);
    }

    void update(int x, int v) {
        update_internal(x, v, 0, 0, n-1);
    }
private:
    vector<int> tree;
    int n;
    int query_internal(int start, int end, int i, int left, int right) {
        if(start > right || end < left) {
            return 0;
        }
        if(start <= left && end >= right) {
            return tree[i];
        }
        int mid = left + (right - left) / 2;
        return max(
            query_internal(start, end, i * 2 + 1, left, mid),
            query_internal(start, end, i * 2 + 2, mid + 1, right)
        );
    }

    void update_internal(int x, int v, int i, int start, int end) {
        if(start > x || end < x) return;
        if(start == end && start == x) {
            tree[i] = v;
            return;
        }
        int mid = start + (end - start) / 2;
        update_internal(x, v, i * 2 + 1, start, mid);
        update_internal(x, v, i * 2 + 2, mid + 1, end);
        tree[i] = max(tree[i*2 + 1], tree[i*2 + 2]);
    }
};
class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        set<int> obstacles;
        obstacles.emplace(0);
        obstacles.emplace(5 * 10000 + 1);
        // Segment Tree keeps track of the max segment from 0 to x
        SegmentTree st(5 * 10000 + 1);
        vector<bool> result;
        for(auto query: queries) {
            int query_type = query[0];
            int x = query[1];
            if(query_type == 1) {
                auto it = obstacles.lower_bound(x);
                auto next_obstacle = *it;
                auto prev_obstacle = *(--it);
                obstacles.emplace(x);
                
                int v = st.query_max(next_obstacle);
                // When there is obstacle added at X
                // Segment Tree needs to update 2 segments, [l, x] and [x, r]
                // with l is obstacle before x, r is obstacle after x 
                st.update(next_obstacle, next_obstacle - x);
                st.update(x, x - prev_obstacle);
            } else {
                int sz = query[2];
                if(st.query_max(x) >= sz) {
                    result.emplace_back(true);
                    continue;
                }
                auto it = obstacles.lower_bound(x);
                auto next_obstacle = *it;
                // if x is not an obstacle
                // Segment Tree will miss the segment [l, x]
                if(next_obstacle != x) {
                    auto prev_obstacle = *(--it);
                    if(x - prev_obstacle >= sz) {
                        result.emplace_back(true);
                        continue;
                    } 
                }
                result.emplace_back(false);
            }
        }
        return result;
    }
};

