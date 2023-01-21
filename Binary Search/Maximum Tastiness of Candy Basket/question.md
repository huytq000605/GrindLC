
# 2517. Maximum Tastiness of Candy Basket<br> Medium

<p>You are given an array of positive integers <code>price</code> where <code>price[i]</code> denotes the price of the <code>i<sup>th</sup></code> candy and a positive integer <code>k</code>.</p>

<p>The store sells baskets of <code>k</code> <strong>distinct</strong> candies. The <strong>tastiness</strong> of a candy basket is the smallest absolute difference of the <strong>prices</strong> of any two candies in the basket.</p>

<p>Return <em>the <strong>maximum</strong> tastiness of a candy basket.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> price = [13,5,1,8,21,2], k = 3
<strong>Output:</strong> 8
<strong>Explanation:</strong> Choose the candies with the prices [13,5,21].
The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
It can be proven that 8 is the maximum tastiness that can be achieved.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> price = [1,3,1], k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> Choose the candies with the prices [1,3].
The tastiness of the candy basket is: min(|1 - 3|) = min(2) = 2.
It can be proven that 2 is the maximum tastiness that can be achieved.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> price = [7,7,7,7], k = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> Choosing any two distinct candies from the candies we have will result in a tastiness of 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= price.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= price[i] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
The answer is binary searchable.
</details>

<details>
<summary> Hint 2 </summary>
For some x, we can use a greedy strategy to check if it is possible to pick k distinct candies with tastiness being at least x.
</details>

<details>
<summary> Hint 3 </summary>
Sort prices and iterate from left to right. For some price[i] check if the price difference between the last taken candy and price[i] is at least x. If so, add the candy i to the basket.
</details>

<details>
<summary> Hint 4 </summary>
So, a candy basket with tastiness x can be achieved if the basket size is bigger than or equal to k.
</details>