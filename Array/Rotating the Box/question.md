# 1861. Rotating the Box<br> Medium

## You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following: A stone '#', A stationary obstacle '*', Empty '.'. The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions. It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box. Return an n x m matrix representing the box after the rotation described above.

Example 1: <br> 
<img src="assets/1.png">
```
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
```

Example 2: <br> 
<img src="assets/2.png">
```
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
```

Example 3: <br> 
<img src="assets/3.png">

```
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
```

Constraints:

m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.-   `1 <= nums.length <= 105`
-   `nums[i] is either 0 or 1.`
-   `0 <= k <= nums.length`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`
-   `Two Pointers`

</details>

<details>

<summary> Hint 1 </summary>
Rotate the box using the relation rotatedBox[i][j] = box[m - 1 - j][i].

</details>
<details>

<summary> Hint 2 </summary>
Start iterating from the bottom of the box and for each empty cell check if there is any stone above it with no obstacles between them.

</details>

