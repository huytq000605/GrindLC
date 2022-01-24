# 1584. Min Cost to Connect All Points<br> Medium

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


Example 1:

<pre>
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
</pre>

Example 2:

<pre>
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
</pre>

Constraints:

- `1 <= points.length <= 1000`
- `-106 <= xi, yi <= 10^6`
- `All pairs (xi, yi) are distinct.`

<details>

<summary> Related Topics </summary>

-   `Graph`
-   `Union Find`

</details>
