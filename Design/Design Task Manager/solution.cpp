class TaskManager {
    unordered_map<int, pair<int, int>> m;
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype([](auto &t1, auto &t2) -> bool {
        if(get<0>(t1) == get<0>(t2)) return get<1>(t1) < get<1>(t2);
        return get<0>(t1) < get<0>(t2);
    })> pq;
public:
    TaskManager(vector<vector<int>>& tasks) {
        for(auto &task: tasks) {
            int u = task[0], t = task[1], p = task[2];
            add(u, t, p);
        }
    }
    
    void add(int userId, int taskId, int priority) {
        m[taskId] = {priority, userId};
        pq.emplace(priority, taskId, userId);
    }
    
    void edit(int taskId, int newPriority) {
        auto &[p, u] = m[taskId];
        add(u, taskId, newPriority);
    }
    
    void rmv(int taskId) {
        m.erase(taskId);
    }
    
    int execTop() {
        while(!pq.empty()) {
            auto [p, t, u] = pq.top();
            pq.pop();
            if(m.find(t) == m.end() || m[t].first != p || m[t].second != u) continue;
            m.erase(t);
            return u;
        }
        return -1;
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
