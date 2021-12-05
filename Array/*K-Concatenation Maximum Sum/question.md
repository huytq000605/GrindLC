# 1191. K-Concatenation Maximum Sum<br> Medium

Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.

Example 1:

<pre>
Input: arr = [1,2], k = 3
Output: 9
</pre>

Example 2:

<pre>
Input: arr = [1,-2,1], k = 5
Output: 2
</pre>

Constraints:

- `1 <= arr.length <= 10^5`
- `1 <= k <= 10^5`
- `-10^4 <= arr[i] <= 10^4`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Kadane's Algorithm`

</details>