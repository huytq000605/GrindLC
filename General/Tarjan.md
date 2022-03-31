# Tarjan Algorithm

## Find all Strong Connected Components (SCC) in directed graph or all Critical Edge for undirected graph 

## Critical Edge
``` python
	graph = [[] for i in range(n)]
	for u, v in connections:
			graph[u].append(v)
			graph[v].append(u)
	# Assume we have graph
	result = []
	idx = 0
	idxs = [-1 for i in range(n)]
	lowest = [-1 for i in range(n)]
	
	def dfs(u, parent):
		nonlocal result, idxs, idx
		idxs[u] = idx
		lowest[u] = idx
		idx += 1
		current = lowest[u]
		for v in graph[u]:
			if v == parent:
				continue
			if idxs[v] == -1:
				lowest_reach = dfs(v, u)
			lowest[u] = min(lowest[u], lowest[v])
			if current < lowest[v]:
				result.append((u, v))
		return lowest[u]
	dfs(0, -1)
	return result
```
							
## SCC
``` python
	graph
	result = []
	idx = 0
	idxs = [-1 for i in range(n)]
	lowest = [-1 for i in range(n)]
	on_stack = [False for i in range(n)]

	def dfs(u):
		nonlocal idxs, idx, lowest, on_stack
		idxs[u] = idx
		lowest[u] = idx
		idx += 1
		for v in graph[u]:
			if idxs[v] == -1:
					lowest_reach = dfs(v, u)
			if on_stack[v]:
				lowest[u] = min(lowest[u], lowest[v])
		if idxs[u] == lowest[u]:
			while True:
				v = stack.pop()
				lowest[v] = u
				on_stack[v] = False
				if v == u:
					break
	dfs(0, -1)
	return lowest # Who have same lowest is in a SCC
```
                    
            