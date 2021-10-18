Can use 2 queue,
let q1, q2

```
while(q1.length) {
	while(q1.length) {
		let node = q1.pop()
		q2.push(node.left)
		q2.push(node.right)
	}
	[q1, q2] = [q2, q1]
}
```