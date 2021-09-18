# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum<br> Medium

Given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.


Example 1:

<pre>
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
</pre>

Example 2:

<pre>
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
</pre>

Constraints:

- `1 <= arr.length <= 10^5`
- `1 <= arr[i] <= 1000`
- `1 <= target <= 10^8`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`
-   `Prefix`

</details>