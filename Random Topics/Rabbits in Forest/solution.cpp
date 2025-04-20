class Solution {
public:
    int numRabbits(vector<int>& answers) {
        int result = 0;
        unordered_map<int, int> m;
        for(int ans: answers) {
            m[ans]++;
            if(ans+1 == m[ans]) {
                m[ans] = 0;
                result += ans+1;
            }
        }
        for(auto &[k, v]: m) {
            if(v) result += k+1;
        }
        return result;
    }
};
