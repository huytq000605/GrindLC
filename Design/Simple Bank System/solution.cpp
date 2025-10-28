class Bank {
vector<long long> b;
public:
    Bank(vector<long long>& balance) {
        for(long long v: balance) {
            b.push_back(v);
        }
    }
    
    bool transfer(int u, int v, long long k) {
        if(!is_valid(u) || !is_valid(v)) return false;
        if(b[u-1] < k) return false;
        b[u-1] -= k;
        b[v-1] += k;
        return true;
    }
    
    bool deposit(int u, long long k) {
        if(!is_valid(u)) return false;
        b[u-1] += k;
        return true;
    }
    
    bool withdraw(int u, long long k) {
        if(!is_valid(u)) return false;
        if(b[u-1] < k) return false;
        b[u-1] -= k;
        return true;
    }
private:
    bool is_valid(int u) {
        return u > 0 && u <= b.size();
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
