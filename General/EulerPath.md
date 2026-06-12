# Euler Path (Eulerian Trail / Hierholzer's Algorithm)

**Idea:** An **Eulerian trail** (or Eulerian path) is a trail in a finite graph that visits **every edge exactly once** (revisiting vertices is allowed). An **Eulerian circuit** (or Eulerian cycle) is an Eulerian trail that starts and ends on the same vertex.

## Properties

Let `in[i]` and `out[i]` denote the in-degree and out-degree of node `i`.

A graph has an Eulerian Path if and only if one of the following holds:

1. `out[i] == in[i]` for every node `i`, and `out[i] % 2 == 0`.
2. `out[i] == in[i]` for all nodes `i` with `out[i] % 2 == 0`, **except** exactly two nodes `x` and `y` where `out[i] % 2 == 1`, with `out[x] == in[x] + 1` and `out[y] == in[y] - 1`.

## Algorithm

1. **Find the starting point** of the Eulerian Path.
   - In case 1 (where `out[i] == in[i]` for all `i`), you can start at an arbitrary node.
2. Perform a **postorder DFS** on the graph. As you "walk" through an edge, **erase** it (or mark it visited) so it is never reused.
3. You may reach the same node many times, but each edge must be passed exactly once.

> In my code I use a stack to erase edges.
