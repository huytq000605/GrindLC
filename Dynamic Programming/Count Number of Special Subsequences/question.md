# 1955. Count Number of Special Subsequences<br> Hard 

A sequence is special if it consists of a positive number of 0s, followed by a positive number of 1s, then a positive number of 2s.

- For example, [0,1,2] and [0,0,1,1,1,2] are special.
- In contrast, [2,1,0], [1], and [0,1,2,0] are not special.
Given an array nums (consisting of only integers 0, 1, and 2), return the number of different subsequences that are special. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are different if the set of indices chosen are different.

Example 1:

<pre>
Input: nums = [0,1,2,2]
Output: 3
Explanation: The special subsequences are [0,1,2,2], [0,1,2,2], and [0,1,2,2].
</pre>

Example 2:

<pre><strong>Input:</strong> nums = [0,1,2,0,1,2]
<strong>Output:</strong> 7
<strong>Explanation:</strong> The special subsequences are:
- [<u>0</u>,<u>1</u>,<u>2</u>,0,1,2]
- [<u>0</u>,<u>1</u>,2,0,1,<u>2</u>]
- [<u>0</u>,<u>1</u>,<u>2</u>,0,1,<u>2</u>]
- [<u>0</u>,<u>1</u>,2,0,<u>1</u>,<u>2</u>]
- [<u>0</u>,1,2,<u>0</u>,<u>1</u>,<u>2</u>]
- [<u>0</u>,1,2,0,<u>1</u>,<u>2</u>]
- [0,1,2,<u>0</u>,<u>1</u>,<u>2</u>]
</pre>

Constraints:

- `1 <= nums.length <= 105`
- `0 <= nums[i] <= 2`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>

