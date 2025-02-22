
# 1756. Design Most Recently Used Queue<br> Medium

<p>Design a queue-like data structure that moves the most recently used element to the end of the queue.</p>

<p>Implement the <code>MRUQueue</code> class:</p>

<ul>
	<li><code>MRUQueue(int n)</code> constructs the <code>MRUQueue</code> with <code>n</code> elements: <code>[1,2,3,...,n]</code>.</li>
	<li><code>int fetch(int k)</code> moves the <code>k<sup>th</sup></code> element <strong>(1-indexed)</strong> to the end of the queue and returns it.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[&quot;MRUQueue&quot;, &quot;fetch&quot;, &quot;fetch&quot;, &quot;fetch&quot;, &quot;fetch&quot;]
[[8], [3], [5], [2], [8]]
<strong>Output:</strong>
[null, 3, 6, 2, 2]

<strong>Explanation:</strong>
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3<sup>rd</sup> element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5<sup>th</sup> element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2<sup>nd</sup> element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8<sup>th</sup> element (2) is already at the end of the queue so just return it.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
	<li>At most <code>2000</code> calls will be made to <code>fetch</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Finding an <code>O(n)</code> algorithm per <code>fetch</code> is a bit easy. Can you find an algorithm with a better complexity for each <code>fetch</code> call?

<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`
-	`Stack`
-	`Design`
-	`Binary Indexed Tree`
-	`Ordered Set`

</details>


<details>
<summary> Hint 1 </summary>
You can store the data in an array and apply each fetch by moving the ith element to the end of the array (i.e, O(n) per operation).
</details>

<details>
<summary> Hint 2 </summary>
A better way is to use the square root decomposition technique.
</details>

<details>
<summary> Hint 3 </summary>
You can build chunks of size sqrt(n). For each fetch operation, You can search for the chunk which has the ith element and update it (i.e., O(sqrt(n)) per operation), and move this element to an empty chunk at the end.
</details>