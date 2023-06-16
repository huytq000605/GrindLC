// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;
impl Solution {
    pub fn max_level_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut result = 0;
        let mut max_value = i32::MIN;
        let mut dq: VecDeque<Rc<RefCell<TreeNode>>> = VecDeque::new();
        dq.push_back(root.unwrap());
        let mut level = 1;
        while dq.len() > 0 {
            let mut value = 0;
            for _ in 0..dq.len() {
                let rc = dq.pop_front().unwrap();
                let node = rc.borrow();
                value += node.val;
                if let Some(left) = &node.left {
                    dq.push_back(left.clone());
                };
                if let Some(right) = &node.right {
                    dq.push_back(right.clone());
                }
            }
            if value > max_value {
                max_value = value;
                result = level;
            }
            level += 1;
        }
        return result
    }
}
