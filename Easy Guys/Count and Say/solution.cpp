class Solution {
public:
    string countAndSay(int n) {
        string result = "1";
        while(--n) {
            string nresult = "";
            char c = result[0], count = 1;
            for(int i = 1; i < result.size(); ++i) {
                if(result[i] == result[i-1]) {
                    ++count;
                } else {
                    nresult += (count + '0');
                    nresult += c;
                    c = result[i];
                    count = 1;
                }
            }
            nresult += (count + '0');
            nresult += c;
            result = nresult;
        }
        return result;
    }
};
