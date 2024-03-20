// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn merge_in_between(mut list1: Option<Box<ListNode>>, a: i32, b: i32, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut cur = list1.as_mut().unwrap();
        for i in 0..a-1 {
            cur = cur.next.as_mut().unwrap();
        }
        std::mem::swap(&mut cur.next, &mut list2);
        while cur.next.is_some() {
            cur = cur.next.as_mut().unwrap();
        }
        for i in 0..b-a+1 {
            list2 = list2.unwrap().next;
        }
        cur.next = list2;
        return list1;
    }
}
