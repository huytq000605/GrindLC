class SegmentTree {
    int n;
    vector<int> freq;
    vector<int> length;
    vector<int> cur_length;

    void build(int i, int l, int r, const vector<int>& x_pos) {
        if(l == r) {
            length[i] = x_pos[r+1] - x_pos[l];
            return;
        }
        int mid = l + (r-l) / 2;
        build(2*i+1, l, mid, x_pos);
        build(2*i+2, mid+1, r, x_pos);
        length[i] = length[i*2+1] + length[i*2+2];
    }

    void update(int i, int l, int r, int ql, int qr, int v) {
        if(qr < l || ql > r) return;
        if(ql <= l && qr >= r) {
            freq[i] += v;
        } else {
            int mid = l + (r - l) / 2;
            update(i*2+1, l, mid, ql, qr, v);
            update(i*2+2, mid+1, r, ql, qr, v);
        }

        if(freq[i]) cur_length[i] = length[i];
        else {
            if(l == r) cur_length[i] = 0;
            else cur_length[i] = cur_length[i*2+1] + cur_length[i*2+2];
        }
    }

public:
    SegmentTree(const vector<int>& x_pos) {
        n = x_pos.size() - 1;
        freq.resize(4*n);
        length.resize(4*n);
        cur_length.resize(4*n);
        build(0, 0, n-1, x_pos);
    }

    int query() {
        return cur_length[0];
    }

    void update(int l, int r, int v){
        update(0, 0, n-1, l, r, v);
    }

};

class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        set<int> x_set;
        squares.reserve(2 * squares.size());
        for(auto &sq: squares) {
            squares.push_back(sq);
            squares.back()[1] += sq[2];
            squares.back()[2] *= -1;
            x_set.insert(sq[0]);
            x_set.insert(sq[0] + sq[2]);
        }

        vector<int> x_pos(x_set.begin(), x_set.end());
        sort(begin(squares), end(squares), [](auto& s1, auto& s2) -> bool {
            return s1[1] < s2[1];
        });
        int n = squares.size();
        SegmentTree st(x_pos);
        int prev_y = squares[0][1];
        vector<long long> areas;
        for(auto &sq: squares) {
            int x = sq[0], y = sq[1], l = sq[2];
            int height = y - prev_y;
            int xstart = lower_bound(begin(x_pos), end(x_pos), x) - begin(x_pos);
            int xend = lower_bound(begin(x_pos), end(x_pos), x + abs(l)) - begin(x_pos) - 1;
            int width = st.query(); 
            areas.push_back((areas.empty() ? 0: areas.back()) + 1LL * width * height);
            st.update(xstart, xend, l > 0 ? 1: -1);
            prev_y = y;
        }

        long long target = (areas.back() + 1) / 2;
        int ind = lower_bound(areas.begin(), areas.end(), target) - areas.begin();
        double ratio = (0.5 * areas.back() - areas[ind-1]) / (areas[ind] - areas[ind-1]);
        return squares[ind-1][1] + (squares[ind][1] - squares[ind-1][1]) * ratio;
    }
};
