class SegmentTree {
public:
    SegmentTree *left, *right;
    int start, end, val, lazy;
    SegmentTree(int s, int e, int v=0, int lazy = 0) {
        start = s;
        end = e;
        val = v;
        left = right = nullptr;
        lazy = 0;
    }

    int query(int s, int e) {
        if(e < start || s > end) return 0;
        if(s <= start && e >= end) return val;
        down();
        return max(left->query(s, e), right->query(s, e));
    }

    void update(int s, int e, int v) {
        if(e < start || s > end) return;
        if(s <= start && e >= end) {
            val = v;
            lazy = 1;
            return;
        };
        down();
        left->update(s, e, v);
        right->update(s, e, v);
        val = max(left->val, right->val);
    }

    void down() {
        if(start != end) {
            if(left == nullptr) {
                int mid = start + (end - start) / 2;
                left = new SegmentTree(start, mid, val);
                right = new SegmentTree(mid+1, end, val);
            }
            if(lazy) {
                left->val = right->val = left->lazy = right->lazy = lazy;
                lazy = 0;
            }
        }
    }
};

class MyCalendar {
public:
SegmentTree *st;
    MyCalendar() {
        st = new SegmentTree(0, pow(10, 9));     
    }
    
    bool book(int start, int end) {
        if(st->query(start, end-1)) {
            return false;
        }
        st->update(start, end-1, 1);
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
