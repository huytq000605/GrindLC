class ZigzagIterator {
vector<int> vv1, vv2;
int i1 = 0, i2 = 0;
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        vv1 = v1;
        vv2 = v2;
    }

    int next() {
        if(i1 >= vv1.size()) return vv2[i2++];
        if(i2 >= vv2.size()) return vv1[i1++];
        if((i1^i2) & 1) return vv2[i2++];
        return vv1[i1++]; 
    }

    bool hasNext() {
        return i1 < vv1.size() || i2 < vv2.size();
    }
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
