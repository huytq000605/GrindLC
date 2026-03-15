class Fancy {
    int mod = 1e9 + 7;
    vector<long long> nums;
    long long inc = 0;
    long long mul = 1;
    long long pow_mod(int x, int power) {
        int result = 1;
        long long base = x;
        int org = power;
        for(; power; power >>= 1) {
            if(power & 1) result = (result * base) % mod;
            base = (base * base) % mod;
        }
        return result;
    }
public:
    Fancy() {
    }
    
    void append(int val) {
        nums.push_back(
            (
                ((val - inc + mod) % mod) * 
                pow_mod(mul, mod-2)
            )
            % mod); 
    }
    
    void addAll(int i) {
        inc = (inc + i) % mod;
    }
    
    void multAll(int m) {
        mul = (mul * m) % mod;
        inc = (inc * m) % mod;  
    }
    
    int getIndex(int idx) {
        if(idx >= nums.size()) return -1;
        return (
            (nums[idx] * mul) % mod + inc
        ) % mod;
    }
};

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy* obj = new Fancy();
 * obj->append(val);
 * obj->addAll(inc);
 * obj->multAll(m);
 * int param_4 = obj->getIndex(idx);
 */
