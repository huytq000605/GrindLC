# Tarjan Algorithm

## Find all Strong Connected Components (SCC) in directed graph or all Critical Edge for undirected graph 

## 1192. Critical Connections in a Network

## Critical Edge
``` python
	graph = [[] for _ in range(n)]
					for u, v in edges:
							graph[u].append(v)
							graph[v].append(u)
	idxs = [-1 for _ in range(n)]
	lowest = [-1 for _ in range(n)]
	i = 0
	result = []
	
	def dfs(u, parent):
			nonlocal i, idxs, lowest, result
			idxs[u] = i
			lowest[u] = i
			i += 1
			for v in graph[u]:
					if v == parent: continue
					if idxs[v] == -1:
							dfs(v, u)
					lowest[u] = min(lowest[u], lowest[v])
					if idxs[u] < lowest[v]:
							result.append((u, v))
```
							
## SCC
``` python
	graph = [[1], [0, 2, 3], [1], [1, 4], [3]]
	result = []
	idx = 0
	idxs = [-1 for i in range(n)]
	lowest = [-1 for i in range(n)]
	stack = []

	def dfs(u, parent):
		nonlocal idxs, idx, lowest, result, stack
		idxs[u] = idx
		lowest[u] = idx
		idx += 1
		stack.append(u)
		for v in graph[u]:
			if v == parent: continue
			if idxs[v] == -1:
					dfs(v, u)
			lowest[u] = min(lowest[u], lowest[v])
		if idxs[u] == lowest[u]:
			component = []
			while True:
				v = stack.pop()
				lowest[v] = u
				component.append(v)
				if v == u:
					result.append(component)
					break
	dfs(0, -1)
	return lowest # Who have same lowest is in a SCC
```
                    
            
