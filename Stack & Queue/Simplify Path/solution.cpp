class Solution {
public:
    string simplifyPath(string path) {
        vector<string> dirs;
        for(int i = 0; i < path.size(); i++) {
            if(path[i] == '/') continue;
            string symbol;
            while(i < path.size() && path[i] != '/') {
                symbol += path[i];
                i += 1;
            }
            if(symbol == ".") {;}
            else if(symbol == "..") {
                if(!dirs.empty()) dirs.pop_back();
            }
            else {
                dirs.emplace_back(symbol);
            }
        }
        if(dirs.empty()) return "/";
        string result = "/";
        for(auto d: dirs) {
            result += d + "/";
        }
        return result.substr(0, result.size() - 1);
    }
};
