use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Node(i32, usize, usize);

impl Solution {
    pub fn k_smallest_pairs(nums1: Vec<i32>, nums2: Vec<i32>, mut k: i32) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::new();
        let (n, m) = (nums1.len(), nums2.len());
        for i in 0..n {
            let (num1, num2) = (nums1[i], nums2[0]);
            heap.push(Node(-num1-num2, i, 0 as usize));
        }
        let mut result = vec![];
        while k > 0 && heap.len() > 0 {
            let Node(_, i1, i2) = heap.pop().unwrap();
            result.push(vec![nums1[i1], nums2[i2]]);
            k -= 1;
            if i2 < m-1 {
                heap.push(Node(-nums1[i1]-nums2[i2+1], i1, i2+1));
            }
        }
        result
    }
}
