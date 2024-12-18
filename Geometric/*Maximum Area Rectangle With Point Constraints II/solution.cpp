class SegmentTree {
    int n;
    vector<int> tree;
public:
    SegmentTree(int _n): n(_n) {
        tree.resize(4*n, -1);
    }

    int query(int start, int end, int i = 0, int left = 0, int right = -1) {
        if(right == -1) right = n-1;
        if(end < left || start > right) return -1;
        if(start <= left && end >= right) return tree[i];
        int mid = left + (right - left) / 2;
        return max(
            query(start, end, i*2+1, left, mid),
            query(start, end, i*2+2, mid+1, right)
        );
    }

    void update(int pos, int value, int i = 0, int left = 0, int right = -1) {
        if(right == -1) right = n-1;
        if(left > pos || right < pos) return;
        if(left == right && left == pos) {
            tree[i] = value;
            return;
        }
        int mid = left + (right - left) / 2;
        update(pos, value, i*2+1, left, mid);
        update(pos, value, i*2+2, mid+1, right);
        tree[i] = max(tree[i*2+1], tree[i*2+2]);
    } 
};

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        vector<pair<int, int>> points(xCoord.size());
        for(int i{}; i < xCoord.size(); ++i) {
            points[i] = make_pair(xCoord[i], yCoord[i]);
        }
        sort(points.begin(), points.end());
        sort(yCoord.begin(), yCoord.end());
        unordered_map<int, int> compressed_y;
        for(int y: yCoord) {
            if(compressed_y.find(y) != compressed_y.end()) continue;
            compressed_y[y] = compressed_y.size();
        }
        //  2     4
        //     5 
        //  1     3
        // check if y_to_max_x equals
        // query [y3, y4] should get x < x3
        unordered_map<int, int> y_to_max_x;
        auto [x3, y3] = points[0];
        long long result{-1};
        SegmentTree st{static_cast<int>(compressed_y.size())};
        for(int i{1}; i < points.size(); ++i) {
            auto [x4, y4] = points[i];
            if(x3 == x4 &&
                y_to_max_x.find(y3) != y_to_max_x.end() && // have (x1, y1), y1 = y3
                y_to_max_x.find(y4) != y_to_max_x.end() && // have (x2, y2), y2 = y4
                y_to_max_x[y3] == y_to_max_x[y4] && // x1 == x2
                st.query(compressed_y[y3] + 1, compressed_y[y4] - 1) < y_to_max_x[y3] // There's no point like 5 
            ) {
                result = max(result, static_cast<long long>(y4 - y3) * (x4 - y_to_max_x[y4]));
            }
            y_to_max_x[y3] = x3;
            st.update(compressed_y[y3], x3);
            swap(x3, x4);
            swap(y3, y4);
        }
        return result;
    }
};
