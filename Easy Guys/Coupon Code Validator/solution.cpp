class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        vector<int> result_index;
        for(int i = 0; i < code.size(); ++i) {
            if(!isActive[i]) continue;
            bool valid = !code[i].empty();
            if(businessLine[i] != "electronics" && businessLine[i] != "grocery" && businessLine[i] != "pharmacy" && businessLine[i] != "restaurant") valid = false;

            if(valid) {
                for(char c: code[i]) {
                    if(!isalpha(c) && !isdigit(c) && c != '_') {
                        valid = false;
                        break;
                    }
                }
            }
            
            if(valid) result_index.push_back(i);
        }        
        auto get_business_idx = [](string& business) {
            if(business == "electronics") return 0;
            else if(business == "grocery") return 1;
            else if(business == "pharmacy") return 2;
            else return 3;
        };
        sort(begin(result_index), end(result_index), [&businessLine, &code, &get_business_idx](auto i1, auto i2) -> bool {
            int bi1 = get_business_idx(businessLine[i1]), bi2 = get_business_idx(businessLine[i2]);
            if(bi1 == bi2) return code[i1] < code[i2];
            return bi1 < bi2;
        });
        vector<string> result;
        for(int i: result_index) {
            result.push_back(code[i]);
        }
        return result;
    }
};
