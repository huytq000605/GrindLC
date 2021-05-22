package main

//Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

/*
Save all num of nums into hashmap
traversal the linkedlist, if node in hashmap then there are component => increase the count to find the rest of component, the component end with a node not in hashmap, increase the result and reset count
then the final, when out of loop, we dont know do we have some last nodes are grouping as a component cause we dont have a node not in hash map at the last to check => check for the last
*/

func numComponents(head *ListNode, nums []int) int {
	numMap := make(map[int]bool)
	result := 0
	count := 0
	for _, num := range nums {
		numMap[num] = true
	}
	for head != nil {
		if _, ok := numMap[head.Val]; ok {
			count++
		} else {
			if count > 0 {
				count = 0
				result++
			}
		}
		head = head.Next
	}
	if count > 0 {
		result++
	}
	return result

}
