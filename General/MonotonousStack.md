# Monotonic Stack

**Idea:** A monotonic stack keeps its elements in a fixed (increasing or decreasing) order. Before pushing a new element, we pop everything that would break that order. This lets us answer "previous/next less/greater element" queries for every element in `O(n)` total.

## What Is a Monotonic Increasing Stack?

Roughly speaking, the elements in a monotonic increasing stack keep an increasing order.

The typical paradigm for a monotonic increasing stack:

```c++
for(int i = 0; i < A.size(); i++){
  while(!in_stk.empty() && in_stk.top() > A[i]){
    in_stk.pop();
  }
  in_stk.push(A[i]);
}
```

## What Can a Monotonic Increasing Stack Do?

1. **Return the max/min elements in some sliding window.**
2. Example:
    - **Find the previous/next less/greater element of each element in a vector in `O(n)` time.**
    - **Find both the previous and next less/greater element of each element.**

When we pop an element, the element at index `i` is its **next greater** element, and the new stack top (`stack[-1]`) is its **previous greater** element:

```python
  stack = []
  arr 
  n = len(arr)
  for i in range(n):
    while len(stack) > 0 and arr[i] > arr[stack[-1]]:
      idxNum = stack.pop()
      nextIdx = i
      prevIdx = stack[-1]
```

## Complexity

- **Time:** `O(n)` — each element is pushed and popped at most once.
- **Space:** `O(n)` for the stack.
