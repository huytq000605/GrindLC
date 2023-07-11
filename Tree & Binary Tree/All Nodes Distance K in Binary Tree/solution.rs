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
    pub fn distance_k(root: Option<Rc<RefCell<TreeNode>>>, target: Option<Rc<RefCell<TreeNode>>>, mut k: i32) -> Vec<i32> {
        let mut parents: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![None; 500];
        
        fn dfs(node: Option<&Rc<RefCell<TreeNode>>>, parent: Option<Rc<RefCell<TreeNode>>>, parents: &mut Vec<Option<Rc<RefCell<TreeNode>>>>) {
            if node.is_none() {
                return
            }
            let rc = node.unwrap();
            let node = rc.borrow();
            parents[node.val as usize] = parent;
            dfs(node.left.as_ref(), Some(rc.clone()), parents);
            dfs(node.right.as_ref(), Some(rc.clone()), parents);
        }
        dfs(root.as_ref(), None, &mut parents);
        
        let mut seen = vec![0; 500];
        seen[target.as_ref().unwrap().borrow().val as usize] = 1;
        let mut dq = std::collections::VecDeque::<Option<Rc<RefCell<TreeNode>>>>::new();
        dq.push_back(target);
        while dq.len() > 0 && k > 0 {
            for _ in 0..dq.len() {
                let cell = dq.pop_front().unwrap();
                if cell.is_none() { 
                    continue 
                }
                let rc = cell.unwrap();
                let node = rc.borrow();
                if let Some(left) = &node.left {
                    let left_br = left.borrow();
                    if seen[left_br.val as usize] == 0 {
                        seen[left_br.val as usize] = 1;
                        dq.push_back(Some(left.clone()));
                    }
                }
                if let Some(right) = &node.right {
                    let right_br = right.borrow();
                    if seen[right_br.val as usize] == 0 {
                        seen[right_br.val as usize] = 1;
                        dq.push_back(Some(right.clone()));
                    }
                }
                if let Some(parent) = &parents[node.val as usize] {
                    let parent_br = parent.borrow();
                    if seen[parent_br.val as usize] == 0 {
                        seen[parent_br.val as usize] = 1;
                        dq.push_back(Some(parent.clone()));
                    }
                }
            } 
            k -= 1;
        }
        
        let mut result = vec![];
        for node in dq {
            result.push(node.unwrap().borrow().val);
        }
        return result
    }
}
