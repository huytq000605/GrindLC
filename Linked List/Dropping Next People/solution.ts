class LLNode {
	value: number
	next: LLNode
	
	constructor(value: number) {
		this.value = value
	}
}

function findingLastOne(n: number) {
	// Cicular Linked List
	let head = new LLNode(0)
	let current = head
	for(let i = 1; i < n; i++) {
		current.next = new LLNode(i)
		current = current.next
	}
	current.next = head

	// Delete all next element until LL only has 1 element
	current = head
	while(current !== current) {
		current.next = current.next.next
		current = current.next
	}
	
	return current.value
}