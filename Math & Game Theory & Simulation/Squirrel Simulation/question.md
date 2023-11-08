
# 573. Squirrel Simulation<br> Medium

<p>You are given two integers <code>height</code> and <code>width</code> representing a garden of size <code>height x width</code>. You are also given:</p>

<ul>
	<li>an array <code>tree</code> where <code>tree = [tree<sub>r</sub>, tree<sub>c</sub>]</code> is the position of the tree in the garden,</li>
	<li>an array <code>squirrel</code> where <code>squirrel = [squirrel<sub>r</sub>, squirrel<sub>c</sub>]</code> is the position of the squirrel in the garden,</li>
	<li>and an array <code>nuts</code> where <code>nuts[i] = [nut<sub>i<sub>r</sub></sub>, nut<sub>i<sub>c</sub></sub>]</code> is the position of the <code>i<sup>th</sup></code> nut in the garden.</li>
</ul>

<p>The squirrel can only take at most one nut at one time and can move in four directions: up, down, left, and right, to the adjacent cell.</p>

<p>Return <em>the <strong>minimal distance</strong> for the squirrel to collect all the nuts and put them under the tree one by one</em>.</p>

<p>The <strong>distance</strong> is the number of moves.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.jpg" style="width: 573px; height: 413px;" />
<pre>
<strong>Input:</strong> height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]
<strong>Output:</strong> 12
<strong>Explanation:</strong> The squirrel should go to the nut at [2, 5] first to achieve a minimal distance.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.jpg" style="width: 253px; height: 93px;" />
<pre>
<strong>Input:</strong> height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= height, width &lt;= 100</code></li>
	<li><code>tree.length == 2</code></li>
	<li><code>squirrel.length == 2</code></li>
	<li><code>1 &lt;= nuts.length &lt;= 5000</code></li>
	<li><code>nuts[i].length == 2</code></li>
	<li><code>0 &lt;= tree<sub>r</sub>, squirrel<sub>r</sub>, nut<sub>i<sub>r</sub></sub> &lt;= height</code></li>
	<li><code>0 &lt;= tree<sub>c</sub>, squirrel<sub>c</sub>, nut<sub>i<sub>c</sub></sub> &lt;= width</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`

</details>


<details>
<summary> Hint 1 </summary>
Will Brute force solution works here? What will be its complexity?
</details>

<details>
<summary> Hint 2 </summary>
Brute force definitely won't work here. Think of some simple solution. Take some example and make some observations.
</details>

<details>
<summary> Hint 3 </summary>
Will order of nuts traversed by squirrel is important or only first nut traversed by squirrel is important?
</details>

<details>
<summary> Hint 4 </summary>
Are there some paths which squirrel have to cover in any case? If yes, what are they?
</details>

<details>
<summary> Hint 5 </summary>
Did you notice only first nut traversed by squirrel matters? Obviously squirrel will choose first nut which will result in minimum distance.
</details>