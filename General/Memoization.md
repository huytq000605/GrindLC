# Memoization Pitfalls

**Idea:** When you cache a result, the cached **value** (not the key) must depend only on the state going *forward* — i.e. the answer from this position to the end. Never cache a value that also depends on something carried from *previous* positions, or the cache entry becomes invalid for other paths that reach the same position.

## Notes

- The values saved into the cache are the results from the current position to the end. Do **not** save a result that has something connected to a previous state mixed in.
- If you feel you need to memoize a previous sum (by folding it into the key), and the question is about a **remainder**, try memoizing the remainder instead of the sum.
