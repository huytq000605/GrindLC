# 817. Linked List Components<br> Medium

### We are given head, the head node of a linked list containing unique integer values. We are also given the list nums, a subset of the values in the linked list. Return the number of connected components in nums, where two values are connected if they appear consecutively in the linked list.You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'. A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string. Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced. Return 0 if the string is already balanced.

 

Example 1:
```
Input: 
head: 0->1->2->3
nums = [0, 1, 3]
Output: 2
Explanation: 
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
```
Example 2:
```
Input: 
head: 0->1->2->3->4
nums = [0, 3, 1, 4]
Output: 2
Explanation: 
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
 ```

Constraints:

* `If n is the length of the linked list given by head, 1 <= n <= 10000.`
* `The value of each node in the linked list will be in the range [0, n - 1].`
* `1 <= nums.length <= 10000.`
* `nums is a subset of all values in the linked list.`
<details>

<summary> Related Topics </summary>

* `Linked List`

</details>