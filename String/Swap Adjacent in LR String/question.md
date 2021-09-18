# 777. Swap Adjacent in LR String<br> Medium

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example 1:

<pre>
Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
</pre>

Example 2:

<pre>
Input: start = "LLR", end = "RRL"
Output: false
</pre>

Constraints:

- `1 <= start.length <= 10^4`
- `start.length == end.length`
- `Both start and end will only consist of characters in 'L', 'R', and 'X'.`

<details>

<summary> Related Topics </summary>

-   `String`

</details>