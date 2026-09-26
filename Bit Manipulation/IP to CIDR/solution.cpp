class Solution {
public:
    long long ip_to_num(string ip) {
        int shift = 24;
        long long result = 0;
        for(long long i = 0, num = 0; i < ip.size(); ++i) {
            if(ip[i] != '.') num = num * 10 + ip[i] - '0';
            if(i == ip.size() - 1 || ip[i] == '.') {
                result += num << shift;
                shift -= 8;
                num = 0;
            }
        }
        return result;
    }

    string num_to_ip(long long num) {
        return std::format("{}.{}.{}.{}", (num >> 24) & 255, (num >> 16) & 255, (num >> 8) & 255, num & 255);
    }
    vector<string> ipToCIDR(string ip, int n) {
        long long num = ip_to_num(ip);
        long long end = num + n - 1;
        vector<string> result;
        while(num <= end) {
            int shifted = 0;
            while(((num & (1 << shifted)) == 0) && (1 << shifted) < end - num + 1) {
                ++shifted;
            }
            if((1 << shifted) > end - num + 1) --shifted;

            result.push_back(format("{}/{}", num_to_ip(num), 32-shifted));
            num += (1 << shifted);
        }
        return result;
    }
};
