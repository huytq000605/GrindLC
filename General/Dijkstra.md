For a problem that have a graph having 2 conditions
Traversal to final node with minimum cost and not having time that > maxTime
So we still use a priority queue (heap) sorted by cost
But we will use a time as distance from source, we update the "distance" when newTime < time[v]
Because we sorted the heap by cost so we will ensure that for each node we traverse through, it has minimum cost
And if the minimum cost path doesn't meet the maxTime condition, we only add node in heap if newTime < maxTime
Then we are sure when we meet the destination node, it has minimum cost and satisfied time