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
    pub fn generate_trees(n: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        fn build(start: i32, end: i32) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
            if start > end {
                return vec![None]
            }
            if start == end {
                let node = TreeNode::new(start);
                return vec![Some(Rc::new(RefCell::new(TreeNode::new(start))))]
            }
            let mut result = vec![];
            for mid in start..end+1 {
                let lefts = build(start, mid-1);
                let rights = build(mid+1, end);
                for left in lefts.iter() {
                    for right in rights.iter() {
                        let mut root = TreeNode::new(mid);
                        root.left = left.clone();
                        root.right = right.clone();
                        result.push(Some(Rc::new(RefCell::new(root))));
                    }
                }
            }
            return result
        }
        return build(1, n)
    }
}
