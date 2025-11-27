/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        unordered_map<int, int> um;
        unordered_map<int, int> counter;
        vector<pair<int, NestedInteger>> st;
        for(auto &l: nestedList) {
            st.emplace_back(1, l);
        }
        int max_depth = 1;
        while(!st.empty()) {
            auto [depth, l] = st.back(); st.pop_back();
            max_depth = max(max_depth, depth);
            if(l.isInteger()) {
                um[l.getInteger()] += depth;
                counter[l.getInteger()] += 1;
            } else {
                for(auto &nl: l.getList()) {
                    st.emplace_back(depth + 1, nl);
                }
            }
        }
        int result = 0;
        for(auto [num, depth]: um) {
            result += num * ((max_depth + 1) * counter[num] - um[num]); 
        }
        return result;
    }
};
