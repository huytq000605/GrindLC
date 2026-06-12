# Dijkstra with Two Constraints (Minimize Cost Under a Time Limit)

**Idea:** For a graph problem with two conditions — reach the destination with **minimum cost** while keeping total time `<= maxTime` — run Dijkstra ordered by cost, and treat **time** as the "distance" you relax on.

## How it works

- Use a priority queue (heap) **sorted by cost**.
- Track `time[v]` as the distance from the source. Update it (relax) only when `newTime < time[v]`.
- Because the heap is ordered by cost, the **first** time we pop any node it is reached with minimum cost.
- To respect the time limit, only push a neighbor into the heap when `newTime < maxTime`. This handles the case where the cheapest path would violate `maxTime` — we simply never explore those states.

So when we pop the destination node, it is guaranteed to have **minimum cost** while also satisfying the **time** condition.
