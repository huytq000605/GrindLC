# Stack (DFS for "Brace" Problems)

**Idea:** For nested parenthesis problems, treat each `(` as a recursive boundary. When you hit an open brace, recurse to process the inner segment; the recursion returns where the outer loop should resume. This avoids the bookkeeping of an explicit stack and keeps each character processed once.

## Optimal: DFS that returns the next index

- Process the string normally.
- On an open `(`, run `dfs`. The `dfs` keeps processing and returns the next index for the outer loop to continue from.

```python
def(string: str):
	def dfs(index):
		while index < len(string):
			...processs...
			if string[index] == ")":
				return [...smt, index]
	
	i = 0
	while i < len(string):
		if string[i] == "(":
			[..., nextIndex] = dfs(i + 1)
			i = nextIndex
		...process...
		i++

```

### Complexity

- **Time:** O(n) — each character is visited once.
- **Space:** O(d) — recursion depth equals the maximum nesting of braces.

## Easy to understand but O(n²)

- Modify the current string in place, because an open brace already in the stack does not change its start index.

```typescript
function(originalString: string) {
	let dfs = (index: number, str: string, stack: number[]) {
		for(let i = index; i < str.length; i++) {
			if(str[i] === "(") stack.push(i)
			if(....)
		}
		// smt happens
		str = str.slice(0, change) + smt + str.slice(afterChange)
		dfs(index + smt.length, str, [...stack]) // The index of open brace still true in stack
	}

}
```

### Complexity

- **Time:** O(n²) — each modification rebuilds the string via `slice`.
- **Space:** O(n) — copied string plus the stack passed into each recursive call.

## Notes

- The key trick in the optimal version: the recursive call **returns the resume index**, so the outer loop skips the already-processed inner segment instead of rescanning it.
- In the O(n²) version, the indices pushed onto `stack` stay valid because the prefix before `index` is never altered.
