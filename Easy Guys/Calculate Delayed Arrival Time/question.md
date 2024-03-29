
# 2651. Calculate Delayed Arrival Time<br> Easy

<p>You are given a positive integer <code>arrivalTime</code> denoting the arrival time of a train in hours, and another positive integer <code>delayedTime</code> denoting the amount of delay in hours.</p>

<p>Return <em>the time when the train will arrive at the station.</em></p>

<p>Note that the time in this problem is in 24-hours format.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arrivalTime = 15, delayedTime = 5 
<strong>Output:</strong> 20 
<strong>Explanation:</strong> Arrival time of the train was 15:00 hours. It is delayed by 5 hours. Now it will reach at 15+5 = 20 (20:00 hours).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arrivalTime = 13, delayedTime = 11
<strong>Output:</strong> 0
<strong>Explanation:</strong> Arrival time of the train was 13:00 hours. It is delayed by 11 hours. Now it will reach at 13+11=24 (Which is denoted by 00:00 in 24 hours format so return 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arrivaltime &lt;&nbsp;24</code></li>
	<li><code>1 &lt;= delayedTime &lt;= 24</code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.
</details>

<details>
<summary> Hint 2 </summary>
If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format.
</details>

<details>
<summary> Hint 3 </summary>
Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.
</details>

<details>
<summary> Hint 4 </summary>
If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format.
</details>