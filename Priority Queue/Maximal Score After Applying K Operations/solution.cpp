class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, less<int>> pq(nums.begin(), nums.end());
        long long result = 0;
        while(k--) {
            int n = pq.top();
            result += n;
            pq.pop();
            pq.emplace((n+2)/3);
        }
        return result;
    }
};
