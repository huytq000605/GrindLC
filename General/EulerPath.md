# Euler Path

In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices). Similarly, an Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex

## Some Properties of Eulerian Path

- in[i] and out[i] to denote the in and out degree of a node i.
- Existence:
  - A graph has an Eulerian Path if and only if 1 or 2
  1. we have out[i] == in[i] for each node i, out[i] % 2 == 0.
  2. we have out[i] == in[i] for all nodes i, out[i] % 2 == 0 except exactly two nodes x and y (% 2 == 1), with out[x] = in[x] + 1, out[y] = in[y] - 1.

## Algorithm

- find the starting point of an Eulerian Path.
  - if 1 we have out[i] == in[i] for all i, we can start at an arbitrary node.
- perform postorder DFS on the graph, as we "walk" through an edge, we erase (or mark it visited) the walked edge.
- we may reach the same node many times, but we have to pass each edge exactly once.
- I use stack in my code for erasing edges.

