# Stack


## DFS in "Brace" questions

### Optimal way:
	- Process a string normal
	- Meet open "(": run dfs, dfs will continue to process, and return the next index for outer

``` python
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

### Easy to understand but O(n^2): 
	- Modify the current string cause open brace in stack doesn't change start


``` typescript
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