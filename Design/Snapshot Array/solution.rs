struct SnapshotArray {
    snap: i32,
    values: Vec<Vec<(i32, i32)>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {

    fn new(length: i32) -> Self {
        return Self{
            snap: 0,
            values: vec![vec![(0, 0)]; length as usize]
        }
    }
    
    fn set(&mut self, index: i32, val: i32) {
        let index = index as usize;
        if self.values[index].len() == 0 || self.values[index].last().unwrap().0 != self.snap {
            self.values[index].push((self.snap, val));
        } else {
            let last = self.values[index].last_mut().unwrap();
            *last = (self.snap, val);
        }
    }
    
    fn snap(&mut self) -> i32 {
        self.snap += 1;
        return self.snap - 1
    }
    
    fn get(&self, index: i32, snap_id: i32) -> i32 {
        let index = index as usize;
        let values = &self.values[index];
        let (mut start, mut end): (usize, usize) = (0, values.len()-1);
        while start < end {
            let mid = start + ((end - start + 1) as f64 / 2.0).ceil() as usize;
            if values[mid].0 > snap_id {
                end = mid - 1;
            } else {
                start = mid;
            }
        }
        return values[start].1
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */
