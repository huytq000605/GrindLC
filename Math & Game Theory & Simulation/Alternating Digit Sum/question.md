
# 2544. Alternating Digit Sum<br> Easy

<p>You are given a positive integer <code>n</code>. Each digit of <code>n</code> has a sign according to the following rules:</p>

<ul>
	<li>The <strong>most significant digit</strong> is assigned a <strong>positive</strong> sign.</li>
	<li>Each other digit has an opposite sign to its adjacent digits.</li>
</ul>

<p>Return <em>the sum of all digits with their corresponding sign</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 521
<strong>Output:</strong> 4
<strong>Explanation:</strong> (+5) + (-2) + (+1) = 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 111
<strong>Output:</strong> 1
<strong>Explanation:</strong> (+1) + (-1) + (+1) = 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 886996
<strong>Output:</strong> 0
<strong>Explanation:</strong> (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<style type="text/css">.spoilerbutton {display:block; border:dashed; padding: 0px 0px; margin:10px 0px; font-size:150%; font-weight: bold; color:#000000; background-color:cyan; outline:0; 
}
.spoiler {overflow:hidden;}
.spoiler > div {-webkit-transition: all 0s ease;-moz-transition: margin 0s ease;-o-transition: all 0s ease;transition: margin 0s ease;}
.spoilerbutton[value="Show Message"] + .spoiler > div {margin-top:-500%;}
.spoilerbutton[value="Hide Message"] + .spoiler {padding:5px;}
</style>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
The first step is to loop over the digits. We can convert the integer into a string, an array of digits, or just loop over its digits.
</details>

<details>
<summary> Hint 2 </summary>
Keep a variable sign that initially equals 1 and a variable answer that initially equals 0.
</details>

<details>
<summary> Hint 3 </summary>
Each time you loop over a digit i, add sign * i to answer, then multiply sign by -1.
</details>