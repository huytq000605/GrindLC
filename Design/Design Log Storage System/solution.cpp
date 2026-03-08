class LogSystem {
vector<pair<int, string>> logs;
public:
    LogSystem() {
        
    }
    
    void put(int id, string timestamp) {
        logs.emplace_back(id, timestamp);
    }
    
    vector<int> retrieve(string start, string end, string granularity) {
        vector<int> result;
        auto sts = parse(start);
        auto ets = parse(end);
        int n = 0;
        if (granularity == "Year") {
            n = 1;
        } else if (granularity == "Month") {
            n = 2;
        } else if (granularity == "Day") {
            n = 3;
        } else if (granularity == "Hour") {
            n = 4;
        } else if (granularity == "Minute") {
            n = 5;
        } else if (granularity == "Second") {
            n = 6;
        }
        for(auto &[id, timestamp]: logs) {
            bool eq_start = true, eq_end = true;
            auto ts = parse(timestamp);
            bool valid = true;
            for(int i = 0; i < n; ++i) {
                if(eq_start && ts[i] < sts[i]) {
                    valid = false;
                    break;
                }
                if(eq_end && ts[i] > ets[i]) {
                    valid = false;
                    break;
                }
                eq_start &= ts[i] == sts[i];
                eq_end &= ts[i] == ets[i];
            }
            if(valid) result.push_back(id);
        }
        return result;
    }


    vector<int> parse(string& timestamp) {
        vector<int> res;
        int cur = 0;
        for(int i = 0; i < timestamp.size(); ++i) {
            if(timestamp[i] == ':') {
                res.push_back(cur);
                cur = 0;
                continue;
            }
            cur = cur * 10 + (timestamp[i] - '0');
        }
        res.push_back(cur);
        return res;
    } 
};

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem* obj = new LogSystem();
 * obj->put(id,timestamp);
 * vector<int> param_2 = obj->retrieve(start,end,granularity);
 */
