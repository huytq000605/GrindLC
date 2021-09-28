# 907. Sum of Subarray Minimums<br> Medium

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

<pre>
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
</pre>

Example 2:

<pre>
Input: arr = [11,81,94,43,3]
Output: 444
</pre>

Constraints:

- `1 <= arr.length <= 3 * 10^4`
- `1 <= arr[i] <= 3 * 10^4`
<details>

<summary> Related Topics </summary>

-   `Monotonous Stack`

</details>