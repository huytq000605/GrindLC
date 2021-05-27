# 1267. Count Servers that Communicate<br> Medium

## You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column. Return the number of servers that communicate with any other server.

Example 1:<br>
<img src="./assets/1.jpg">

```
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
```
Example 2:<br>
<img src="./assets/2.jpg">

```
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
 ```

Example 3:<br>
<img src="./assets/3.jpg">

```
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 ```



Constraints:

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m <= 250`
* `1 <= n <= 250`
* `grid[i][j] == 0 or 1`

<details>

<summary> Related Topics </summary>

* `Array` 

</details>

<details>

<summary> Hint 1 </summary>
Store number of computer in each row and column.

</details>

<details>

<summary> Hint 2 </summary>
Count all servers that are not isolated.

</details>