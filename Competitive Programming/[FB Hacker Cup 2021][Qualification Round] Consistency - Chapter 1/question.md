# Problem A: Cryptoconference


Connie received a string SS for her birthday, consisting entirely of uppercase letters (each between "A" and "Z", inclusive).
However, Connie really only likes nice, consistent strings. She considers a string to be consistent if and only if all of its letters are the same.
Each second, Connie may choose one letter in SS and replace it with a different letter. If her chosen letter is a vowel, then she may replace it with any consonant of her choice. On the other hand, if her chosen letter is a consonant, then she may replace it with any vowel of her choice. The 55 letters "A", "E", "I", "O", and "U" are considered vowels, while the remaining 2121 letters of the alphabet are considered consonants. If a letter appears multiple times in SS, she may only replace a single occurrence per second.
Help her determine the minimum number of seconds required to change SS into any consistent string. Note that SS might already be consistent, in which case 00 seconds would be required.

**Constraints**


- `1 <= T <= 45`
- `1 <= |S| <= 100`
- `"A" <= Si <= "Z"`


The sum of |S| across all test cases is at most 4500.

**Input**

Input begins with an integer TT, the number of birthdays Connie has had. For each birthday, there is a single line containing the string SS.

**Output**

For the iith string, print a line containing "Case #i: " followed by the minimum number of seconds required to change SS into any consistent string.

**Sample Explanation**

In the first case, Connie could replace the second and third letters ("B" and "C") each with "A", yielding the string "AAA" in 22 seconds.

In the second case, "F" is already consistent.

In the third case, Connie could replace the first, third, and fifth letters ("B", "N", and "N") each with "A", yielding the string "AAAAAA" in 33 seconds.

**Sample Input**
<pre>
6
ABC
F
BANANA
FBHC
FOXEN
CONSISTENCY
</pre>

**Sample Output**
<pre>
Case #1: 2
Case #2: 0
Case #3: 3
Case #4: 4
Case #5: 5
Case #6: 12
</pre>