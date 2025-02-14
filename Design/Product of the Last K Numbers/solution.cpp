class ProductOfNumbers {
vector<int> nums{1};
public:
    ProductOfNumbers() {
        
    }
    
    void add(int num) {
        if(num == 0) nums = {1};
        else nums.emplace_back(nums.back() * num);
    }
    
    int getProduct(int k) {
        int n = nums.size();
        if(n-k-1 < 0) return 0;
        return nums[n-1] / nums[n-k-1];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */
