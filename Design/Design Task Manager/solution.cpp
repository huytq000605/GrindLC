class TaskManager {
public:
// task, priority
unordered_map<int, int> um;
// task, priority, user
priority_queue<
    pair<int, int>, 
    vector<pair<int, int>>, 
    decltype([](auto &t1, auto &t2) -> bool {
        if(t1.second == t2.second) return t1.first < t2.first;
        return t1.second < t2.second;
    })> pq;
unordered_map<int, int> tu;
    TaskManager(vector<vector<int>>& tasks) {
        for(auto &task: tasks) {
            int u = task[0];
            int t = task[1];
            int p = task[2];
            add(u, t, p);
        }
    }
    
    void add(int userId, int taskId, int priority) {
        pq.emplace(taskId, priority);
        um[taskId] = priority;
        tu[taskId] = userId;
    }
    
    void edit(int taskId, int newPriority) {
        um[taskId] = newPriority;
        int u = tu[taskId];
        pq.emplace(taskId, newPriority);
    }
    
    void rmv(int taskId) {
        um.erase(taskId);
        tu.erase(taskId);
    }
    
    int execTop() {
        while(!pq.empty()) {
            auto [t, p] = pq.top();
            if(um.find(t) == um.end() || um[t] != p) {
                pq.pop();
                continue;
            }
            break;
        }
        if(pq.empty()) return -1;
        auto [t, p] = pq.top(); pq.pop();
        int u = tu[t];
        rmv(t);
        return u;
    }
};

/**
 * Your TaskManager object will be instantiated and called as such:
 * TaskManager* obj = new TaskManager(tasks);
 * obj->add(userId,taskId,priority);
 * obj->edit(taskId,newPriority);
 * obj->rmv(taskId);
 * int param_4 = obj->execTop();
 */
