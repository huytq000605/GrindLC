/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	firstEven := head.Next
	firstOdd := head
	lastOdd := head
	idx := 1
	for {
		if head.Next != nil {
			next := head.Next
			head.Next = head.Next.Next
			if idx%2 == 1 {
				if head.Next != nil {
					lastOdd = head.Next
				} else {
					lastOdd = head
				}
			}
			head = next
			idx++
		} else {
			break
		}
	}
	lastOdd.Next = firstEven
	return firstOdd
}