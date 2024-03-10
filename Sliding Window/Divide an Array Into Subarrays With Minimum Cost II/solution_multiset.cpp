class Solution {
public:
    long long minimumCost(vector<int>& nums, int k, int dist) {
        int n = nums.size();
        long long cur = nums[0];
        k--;
        multiset<long long> active;
        multiset<long long> inactive;
        for (int i = 1; i <= dist + 1; i++) {
            cur += nums[i];
            active.insert(nums[i]);
        }
        while (active.size() > k) {
            inactive.insert(*active.rbegin());
            cur -= *active.rbegin();
            active.erase(active.find(*active.rbegin()));
        }
        long long result = cur;
        for (int i = dist + 2; i < n; i++) {
            if (active.find(nums[i-dist-1]) != active.end()) {
                active.erase(active.find(nums[i-dist-1]));
                cur -= nums[i-dist-1];
            } else {
                inactive.erase(inactive.find(nums[i-dist-1]));
            }

            if (nums[i] < *active.rbegin()) {
                active.insert(nums[i]);
                cur += nums[i];
            } else {
                inactive.insert(nums[i]);
            }
            
            if (active.size() > k) {
                cur -= *active.rbegin();
                inactive.insert(*active.rbegin());
                active.erase(active.find(*active.rbegin()));
            }

            if (active.size() < k) {
                cur += *inactive.begin();
                active.insert(*inactive.begin());
                inactive.erase(inactive.find(*inactive.begin()));
            }
            result = min(result, cur);
        }
        return result;
    }
};
