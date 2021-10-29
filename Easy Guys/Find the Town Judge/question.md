# 997. Find the Town Judge<br> Easy

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

- The town judge trusts nobody.
- Everybody (except for the town judge) trusts the town judge.
- There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

<pre>
Input: n = 2, trust = [[1,2]]
Output: 2
</pre>

Example 2:

<pre>
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
</pre>

Constraints:

- `1 <= n <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `All the pairs of trust are unique.`
- `ai != bi`
- `1 <= ai, bi <= n`

<details>

<summary> Related Topics </summary>

-   `Array`

</details>