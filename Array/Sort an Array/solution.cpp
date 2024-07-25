class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        auto msort = [&](int start, int end, auto & msort_ref) -> vector<int> {
            if(start == end) return {nums[start]};
            else if(start > end) return {};
            int mid = start + (end - start) / 2;
            vector<int> left = msort_ref(start, mid, msort_ref);
            vector<int> right = msort_ref(mid + 1, end, msort_ref);
            int i = 0, j = 0;
            vector<int> result;
            while(i < left.size() || j < right.size()) {
                if(i >= left.size()) result.emplace_back(right[j++]);
                else if(j >= right.size()) result.emplace_back(left[i++]);
                else if(left[i] <= right[j]) result.emplace_back(left[i++]);
                else result.emplace_back(right[j++]);
            }
            return result;
        };
        return msort(0, nums.size() - 1, msort);
        return nums;
    }
};
