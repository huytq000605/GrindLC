class KthLargest {
    vector<int> nums;
    int k;
public:
    KthLargest(int k, vector<int>& nums) {
        vector<int> arr;
        arr.reserve(k);

        for(auto num: nums) {
            arr.emplace_back(num);
            push_heap(arr.begin(), arr.end(), greater<int>());
            if(arr.size() > k) {
                pop_heap(arr.begin(), arr.end(), greater<int>());
                arr.pop_back();
            }
        }
        this->nums = arr;
        this->k = k;
    }
    
    int add(int val) {
        nums.emplace_back(val);
        push_heap(nums.begin(), nums.end(), greater<int>());
        if(nums.size() > k) {
            pop_heap(nums.begin(), nums.end(), greater<int>());
            nums.pop_back();
        }
        return nums[0];
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
