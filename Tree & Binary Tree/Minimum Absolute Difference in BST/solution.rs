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
impl Solution {
    pub fn get_minimum_difference(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (mut result, mut prev) = (i32::MAX, None);
        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, prev: &mut Option<i32>, result: &mut i32) {
            if let None = node {
                return
            }
            let rc_ref = node.unwrap();
            let node = rc_ref.borrow();

            dfs(node.left.clone(), prev, result);
            if let Some(prev) = *prev {
                *result = std::cmp::min(*result, node.val - prev);
            }
            *prev = Some(node.val);
            dfs(node.right.clone(), prev, result)
        }
        dfs(root, &mut prev, &mut result);
        return result
    }
}
