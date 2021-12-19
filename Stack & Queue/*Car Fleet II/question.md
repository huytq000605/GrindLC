# 1776. Car Fleet II<br> Hard

There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

- positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
- speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

Example 1:

<pre>
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
</pre>

Example 2:

<pre>
Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
</pre>

Constraints:

- `1 <= cars.length <= 10^5`
- `1 <= positioni, speedi <= 10^6`
- `positioni < positioni+1`

<details>

<summary> Related Topics </summary>

-   `Monotonic Stack`
-   `Greedy`

</details>

<details>

<summary> Hint 1 </summary>
We can simply ignore the merging of any car fleet, simply assume they cross each other. Now the aim is to find the first car to the right, which intersects with the current car before any other.
</details>
<details>

<summary> Hint 2 </summary>
Assume we have already considered all cars to the right already, now the current car is to be considered. Let’s ignore all cars with speeds higher than the current car since the current car cannot intersect with those ones. Now, all cars to the right having speed strictly less than current car are to be considered. Now, for two cars c1 and c2 with positions p1 and p2 (p1 < p2) and speed s1 and s2 (s1 > s2), if c1 and c2 intersect before the current car and c2, then c1 can never be the first car of intersection for any car to the left of current car including current car. So we can remove that car from our consideration.
</details>

<details>
<summary> Hint 3 </summary>
We can see that we can maintain candidate cars in this way using a stack, removing cars with speed greater than or equal to current car, and then removing cars which can never be first point of intersection. The first car after this process (if any) would be first point of intersection.
</details>
