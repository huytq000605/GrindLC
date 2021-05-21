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
1. **Find the previous less element of each element in a vector with O(n) time:**<br>
What is the previous less element of an element?<br>
For example:<br>
[3, 7, 8, 4]<br>
The previous less element of 7 is 3.<br>
The previous less element of 8 is 7.<br>
The previous less element of 4 is 3.<br>
There is no previous less element for 3.<br>
For simplicity of notation, we use abbreviation PLE to denote Previous Less Element.<br>

C++ code (by slitghly modifying the paradigm):<br>
Instead of directly pushing the element itself, here for simplicity, we push the index. We do some record when the index is pushed into the stack.
``` c++
// previous_less[i] = j means A[j] is the previous less element of A[i].
// previous_less[i] = -1 means there is no previous less element of A[i].
vector<int> previous_less(A.size(), -1);
for(int i = 0; i < A.size(); i++){
  while(!in_stk.empty() && A[in_stk.top()] > A[i]){
    in_stk.pop();
  }
  previous_less[i] = in_stk.empty()? -1: in_stk.top();
  in_stk.push(i);
}
```
---

2. **Find the next less element of each element in a vector with O(n) time:**<br>
What is the next less element of an element?<br>
For example:<br>
[3, 7, 8, 4]<br>
The next less element of 8 is 4.<br>
The next less element of 7 is 4.<br>
There is no next less element for 3 and 4.<br>
For simplicity of notation, we use abbreviation NLE to denote Next Less Element.

C++ code (by slighly modifying the paradigm):<br>
We do some record when the index is poped out from the stack.

``` c++
// next_less[i] = j means A[j] is the next less element of A[i].
// next_less[i] = -1 means there is no next less element of A[i].
vector<int> previous_less(A.size(), -1);
for(int i = 0; i < A.size(); i++){
  while(!in_stk.empty() && A[in_stk.top()] > A[i]){
    auto x = in_stk.top(); in_stk.pop();
    next_less[x] = i;
  }
  in_stk.push(i);
}
```