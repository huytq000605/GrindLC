# Noted for myself

Signal for a problem about binary search tree is that you can get the range minimum to maximum of answer, find a value that fit condition for an sorted array

So when you try do BST, compare the current value you are using to condition, the ">" and "<" is easy to put in, but the "=" is a little tricky

Like when question ask you for a minimum index in an arr (SORTED BY ASC) that arr[index] < 5, if arr[current] >= 5 YOU MUST SET THE NEXT LOOP IS max = current - 1 BECAUSE current doesnt fit in condition


**IMPORTANT**
```
As a rule of thumb, use m = l + (r-l)/ 2 with l = m + 1 and r = m, and use m = l + (r-l+1)/2 with l = m and r = m - 1. This can prevent m from stucking at r (or l) after the updating step.
```

Example: When the problem asks you for finding min for condition, if the value is fit for the condition, you can keep decrease/increase the max/min to get the real min answer

Example with Find the smallest divisor given a threshold: 
    If sum <= threshold then can keep decrease the max value to find a more smaller divisior that fit the condition
    If sum > threshold then we are sure that the current value we are using is wrong, then just let min = mid + 1


THE FINAL ANSWER SHOULD BE WHEN MIN = MAX 

# Precision Binary Search
```
double lo = initial_lo; // Set initial lower bound
double hi = initial_hi; // Set initial upper bound
double eps = 1e-5;      // Tolerance level

while (hi - lo > eps) {
    double mid = (lo + hi) / 2.0;
    if (condition(mid)) {
        lo = mid; // or adjust hi based on your condition
    } else {
        hi = mid;
    }
}
double answer = (lo + hi) / 2.0;
```
