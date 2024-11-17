# We introduce a very important stack type, which is called monotone stack .

## What is monotonous increase stack?
Roughly speaking, the elements in the an monotonous increase stack keeps an increasing order.

**The typical paradigm for monotonous increase stack:**
``` c++
for(int i = 0; i < A.size(); i++){
  while(!in_stk.empty() && in_stk.top() > A[i]){
    in_stk.pop();
  }
  in_stk.push(A[i]);
}
```

## What can monotonous increase stack do?
1. **Return the max/min elements in some sliding window**
2. Example:
    - **Find the previous/next less/greater element of each element in a vector with O(n) time:**
    - **Find both previous and next less/greater element of each element**
``` python
  stack = []
  arr 
  n = len(arr)
  for i in range(n):
    while len(stack) > 0 and arr[i] > arr[stack[-1]]:
      idxNum = stack.pop()
      nextIdx = i
      prevIdx = stack[-1]
```
  
