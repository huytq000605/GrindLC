# 93. Restore IP Addresses<br> Medium

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 


Example 1:

<pre>
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
</pre>

Example 2:

<pre>
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>

Constraints:

- `0 <= s.length <= 3000`
- `s consists of digits only.`

<details>

<summary> Related Topics </summary>

-   `Backtrack`
-   `String`

</details>