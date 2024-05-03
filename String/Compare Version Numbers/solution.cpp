class Solution {
public:
    int compareVersion(string version1, string version2) {
        auto get_revs = [](string version) -> vector<int> {
            vector<int> revs;
            long cur = 0;
            for(char & c: version) {
                if(c == '.') {
                    revs.emplace_back(cur);
                    cur = 0;
                } else {
                    cout << cur << " " << c - '0' << endl;
                    cur = cur * 10 + c - '0';
                }
            }
            revs.emplace_back(cur);
            return revs;
        };

        auto revs1 = get_revs(version1);
        auto revs2 = get_revs(version2);
        int i = 0, j = 0;
        while(i < revs1.size() || j < revs2.size()) {
            int rev1 = 0, rev2 = 0;
            if(i < revs1.size()) rev1 = revs1[i++];
            if(j < revs2.size()) rev2 = revs2[j++];
            if(rev1 < rev2) return -1;
            else if(rev1 > rev2) return 1;
        }
        return 0;
        
    }
};
