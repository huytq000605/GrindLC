class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        unordered_map<int, int> mods;
        for(auto num: arr) {
            num %= k;
            if(num == 0) continue;
            if(num < 0) num += k;
            if(mods.find(k - num) != mods.end()) {
                mods[k-num] == 1 ? mods.erase(k-num) : --mods[k-num];
            } else ++mods[num];
        }
        return mods.empty();
    }
};
