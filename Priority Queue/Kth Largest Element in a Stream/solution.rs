use std::collections::BinaryHeap;

struct KthLargest {
    pq: BinaryHeap<i32>,
    k: i32
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {

    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut pq = BinaryHeap::new();
        for num in nums {
            pq.push(-num);
            if pq.len() > k as usize {
                pq.pop();
            }
        }
        return KthLargest{pq: pq, k: k}
    }
    
    fn add(&mut self, val: i32) -> i32 {
        self.pq.push(-val);
        if self.pq.len() > self.k as usize {
            self.pq.pop();
        }        
        return -*self.pq.peek().unwrap()
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */
