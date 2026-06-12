# Tree Rerooting (Rerooting Technique)

**Idea:** Use this when the problem asks you to aggregate some information for *every* node as if that node were the root. Run a DFS once from a fixed root to compute the answer for that root, then do a second pass that derives each child's answer from its parent's by figuring out how the aggregated information changes when the root shifts from a node to its child.

## Why It Works

Recomputing the answer independently for every root is expensive. Instead, find the relationship between a node's answer and its child's answer, so the answer can be "rerooted" from parent to child in `O(1)` during a top-down pass.

## Example

- #3241. Time Taken to Mark All Nodes
