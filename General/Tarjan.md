# Tarjan's Algorithm (Bridges & Strongly Connected Components)

**Idea:** A single DFS that assigns each node a discovery index (`idxs`) and tracks the lowest index reachable from its subtree (`lowest`). Comparing these two values reveals **critical edges (bridges)** in an undirected graph and **strongly connected components (SCC)** in a directed graph.

The key quantities:
- `idxs[u]` — the order in which `u` was first visited (its discovery time).
- `lowest[u]` — the smallest discovery index reachable from `u` (including via back edges through its subtree).

Related problem: **1192. Critical Connections in a Network**.

## Critical Edge (Bridge — Undirected Graph)

An edge `(u, v)` is a bridge when nothing in `v`'s subtree can reach back to `u` or earlier, i.e. `idxs[u] < lowest[v]`.

```python
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

## SCC (Directed Graph)

A node `u` is the root of an SCC when `idxs[u] == lowest[u]`. At that point, pop the DFS stack down to `u` to collect the whole component.

```python
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

After the run, nodes that share the same `lowest` value belong to the same SCC.

## Complexity

- **Time:** O(V + E) — one DFS over all vertices and edges.
- **Space:** O(V) — `idxs`, `lowest`, the stack, and the recursion depth.
