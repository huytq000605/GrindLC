class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> result;

        // recursive
        // auto dfs = [&](int cur, auto dfs) -> void {
        //     result.emplace_back(cur);
        //     if(cur * 10 <= n) dfs(cur * 10, dfs);
        //     if(cur % 10 != 9 && cur + 1 <= n) dfs(cur+1, dfs); 
        // };
        // dfs(1, dfs);
        // return result;

        // iterative
        int cur = 1;
        for(int i = 0; i < n; ++i) {
            result.emplace_back(cur);
            if(cur * 10 <= n) cur = cur * 10;
            else {
                if(cur % 10 != 9 && cur+1 <= n) ++cur;
                else {
                    while(cur == n || cur % 10 == 9) cur /= 10;
                    ++cur;
                }
            }
        }
        return result;
    }
};
