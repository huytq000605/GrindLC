# 1703. Minimum Adjacent Swaps for K Consecutive Ones<br> Hard

You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.

Example 1:

<pre>
Input: nums = [1,0,0,1,0,1], k = 2
Output: 1
Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
</pre>

Example 2:

<pre>
Input: nums = [1,0,0,0,0,0,1,1], k = 3
Output: 5
Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
</pre>

Constraints:

- `1 <= nums.length <= 10^5`
- `nums[i] is 0 or 1.`
- `1 <= k <= sum(nums)`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`
-   `Array`

</details>

<details>

<summary> Hint 1 </summary>
Choose k 1s and determine how many steps are required to move them into 1 group.
</details>
<details>

<summary> Hint 2 </summary>
Maintain a sliding window of k 1s, and maintain the steps required to group them.
</details>

<details>
<summary> Hint 3 </summary>
When you slide the window across, should you move the group to the right? Once you move the group to the right, it will never need to slide to the left again.
</details>
