class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int lo{1}, hi{static_cast<int>(nums.size())/2};
        while(lo < hi) {
            int k{lo + (hi-lo+1)/2};
            int pa{nums[0]}, pb{nums[k]};
            int cnt{1};
            bool valid{false};
            for(int a{1}; a < nums.size() - k; ++a) {
                if(nums[a] <= pa || nums[a+k] <= pb) {
                    cnt = 0;
                }
                ++cnt;
                if(cnt == k) {
                    valid = true;
                    break;
                }
                pa = nums[a];
                pb = nums[a+k];
            }
            if(!valid) {
                hi = k-1;
            } else {
                lo = k;
            }
        }
        
        return lo;
    }
};
