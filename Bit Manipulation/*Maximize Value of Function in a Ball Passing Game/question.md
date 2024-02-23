
# 2836. Maximize Value of Function in a Ball Passing Game<br> Hard

<p>You are given a <strong>0-indexed</strong> integer array <code>receiver</code> of length <code>n</code> and an integer <code>k</code>.</p>

<p>There are <code>n</code> players having a <strong>unique id</strong> in the range <code>[0, n - 1]</code> who will play a ball passing game, and <code>receiver[i]</code> is the id of the player who receives passes from the player with id <code>i</code>. Players can pass to themselves, <strong>i.e.</strong> <code>receiver[i]</code> may be equal to <code>i</code>.</p>

<p>You must choose one of the <code>n</code> players as the starting player for the game, and the ball will be passed <strong>exactly</strong> <code>k</code> times starting from the chosen player.</p>

<p>For a chosen starting player having id <code>x</code>, we define a function <code>f(x)</code> that denotes the <strong>sum</strong> of <code>x</code> and the <strong>ids</strong> of all players who receive the ball during the <code>k</code> passes, <strong>including repetitions</strong>. In other words, <code>f(x) = x + receiver[x] + receiver[receiver[x]] + ... + receiver<sup>(k)</sup>[x]</code>.</p>

<p>Your task is to choose a starting player having id <code>x</code> that <strong>maximizes</strong> the value of <code>f(x)</code>.</p>

<p>Return <em>an integer denoting the <strong>maximum</strong> value of the function.</em></p>

<p><strong>Note:</strong> <code>receiver</code> may contain duplicates.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<th style="padding: 5px; border: 1px solid black;">Pass Number</th>
			<th style="padding: 5px; border: 1px solid black;">Sender ID</th>
			<th style="padding: 5px; border: 1px solid black;">Receiver ID</th>
			<th style="padding: 5px; border: 1px solid black;">x + Receiver IDs</th>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">0</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">0</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">5</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">4</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

<pre>
<strong>Input:</strong> receiver = [2,0,1], k = 4
<strong>Output:</strong> 6
<strong>Explanation:</strong> The table above shows a simulation of the game starting with the player having id x = 2. 
From the table, f(2) is equal to 6. 
It can be shown that 6 is the maximum achievable value of the function. 
Hence, the output is 6. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<th style="padding: 5px; border: 1px solid black;">Pass Number</th>
			<th style="padding: 5px; border: 1px solid black;">Sender ID</th>
			<th style="padding: 5px; border: 1px solid black;">Receiver ID</th>
			<th style="padding: 5px; border: 1px solid black;">x + Receiver IDs</th>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">&nbsp;</td>
			<td style="padding: 5px; border: 1px solid black;">4</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">4</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">7</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">9</td>
		</tr>
		<tr>
			<td style="padding: 5px; border: 1px solid black;">3</td>
			<td style="padding: 5px; border: 1px solid black;">2</td>
			<td style="padding: 5px; border: 1px solid black;">1</td>
			<td style="padding: 5px; border: 1px solid black;">10</td>
		</tr>
	</tbody>
</table>

<pre>
<strong>Input:</strong> receiver = [1,1,1,2,3], k = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> The table above shows a simulation of the game starting with the player having id x = 4. 
From the table, f(4) is equal to 10. 
It can be shown that 10 is the maximum achievable value of the function. 
Hence, the output is 10. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= receiver.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= receiver[i] &lt;= n - 1</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>10</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
<div class="_1l1MA">We can solve the problem using binary lifting.</div>
</details>

<details>
<summary> Hint 2 </summary>
<div class="_1l1MA">For each player with id <code>x</code> and for every <code>i</code> in the range <code>[0, ceil(log<sub>2</sub>k)]</code>, we can determine the last receiver's id and compute the sum of player ids who receive the ball after <code>2<sup>i</sup></code> passes, starting from <code>x</code>.</div>
</details>

<details>
<summary> Hint 3 </summary>
<div class="_1l1MA">Let <code>last_receiver[x][i] =</code> the last receiver's id after <code>2<sup>i</sup></code> passes, and <code>sum[x][i] =</code> the sum of player ids who receive the ball after <code>2<sup>i</sup></code> passes. For all <code>x</code> in the range <code>[0, n - 1]</code>, <code>last_receiver[x][0] = receiver[x]</code>, and <code>sum[x][0] = receiver[x]</code>.</div>
</details>

<details>
<summary> Hint 4 </summary>
<div class="_1l1MA">Then for <code>i</code> in range <code>[1, ceil(log<sub>2</sub>k)]</code>, <code>last_receiver[x][i] = last_receiver[last_receiver[x][i - 1]][i - 1]</code> and <code>sum[x][i] = sum[x][i - 1] + sum[last_receiver[x][i - 1]][i - 1]</code>, for all <code>x</code> in the range <code>[0, n - 1]</code>.</div>
</details>

<details>
<summary> Hint 5 </summary>
<div class="_1l1MA">Starting from each player id <code>x</code>, we can now go through the powers of <code>2</code> in the binary representation of <code>k</code> and make jumps corresponding to each power, using the pre-computed values, to compute <code>f(x)</code>.</div>
</details>

<details>
<summary> Hint 6 </summary>
<div class="_1l1MA">The answer is the maximum <code>f(x)</code> from each player id.</div>
</details>