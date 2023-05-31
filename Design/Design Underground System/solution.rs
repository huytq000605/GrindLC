use std::collections::HashMap;

struct UndergroundSystem {
    customers: HashMap<i32, (String, i32)>,
    records: HashMap<String, HashMap<String, (i32, i32)>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl UndergroundSystem {

    fn new() -> Self {
        UndergroundSystem {
            customers: HashMap::new(),
            records: HashMap::new()
        }
    }
    
    fn check_in(&mut self, id: i32, station_name: String, t: i32) {
        self.customers.insert(id, (station_name, t));
    }
    
    fn check_out(&mut self, id: i32, end: String, t2: i32) {
        let (start, t1) = self.customers.get(&id).unwrap();
        self.records.entry(start.to_string()).
            or_insert(HashMap::new()).
            entry(end).
            and_modify(|tup| *tup = (tup.0 + t2 - t1, tup.1 + 1)).
            or_insert((t2 - t1, 1));
        
    }
    
    fn get_average_time(&self, start: String, end: String) -> f64 {
        let (times, n) = *self.records.get(&start).unwrap().get(&end).unwrap();
        return times as f64 / n as f64
    }
}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * let obj = UndergroundSystem::new();
 * obj.check_in(id, stationName, t);
 * obj.check_out(id, stationName, t);
 * let ret_3: f64 = obj.get_average_time(startStation, endStation);
 */
