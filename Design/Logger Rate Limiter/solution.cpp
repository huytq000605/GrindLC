class Logger {
unordered_map<string, int> logged;
public:
    Logger() {
    }
    
    bool shouldPrintMessage(int timestamp, string message) {
        if(logged.find(message) == logged.end() || logged[message] <= timestamp - 10) {
            logged[message] = timestamp;
            return true;
        }
        return false;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */
