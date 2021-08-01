# 42. Trapping Rain Water<br> Hard

## Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

![](assets/rainwatertrap.png)

<pre>
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

Example 2:

<pre>
Input: height = [4,2,0,3,2,5]
Output: 9
</pre>

Constraints:

- `n == height.length`
- `0 <= n <= 3 * 104`
- `0 <= height[i] <= 105`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `Monotonic Stack`

</details>
