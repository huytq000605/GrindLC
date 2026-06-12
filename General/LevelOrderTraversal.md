# Level Order Traversal (Two-Queue BFS)

**Idea:** Process a binary tree level by level using two queues. `q1` holds all nodes of the current level; as you pop them, push their children into `q2`. When `q1` is empty, the level is done — swap the queues and repeat with the next level.

```javascript
while(q1.length) {
	while(q1.length) {
		let node = q1.pop()
		q2.push(node.left)
		q2.push(node.right)
	}
	[q1, q2] = [q2, q1]
}
```

## Notes

- Each pass of the inner loop drains one full level, so the boundary between levels is implicit (no need to track level sizes).
- After the swap, `q2` becomes the new empty buffer for the next level's children.

## Complexity

- **Time:** O(n) — each node is enqueued and dequeued once.
- **Space:** O(n) — up to a full level (the widest level) is held across the two queues.
