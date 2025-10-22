class SparseVector {
public:
    vector<pair<int, int>> v;
    SparseVector(vector<int> &nums) {
        for(int i = 0; i < nums.size(); ++i) {
            if(nums[i]) v.emplace_back(i, nums[i]);
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        auto &v2 = vec.v;
        int result = 0;
        for(int i = 0, j = 0; i < v.size() && j < v2.size();) {
            if(v[i].first == v2[j].first) {
                result += v[i++].second * v2[j++].second;
            } else {
                if(v[i].first > v2[j].first) ++j;
                else ++i;
            }
        }
        return result;
    }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);
