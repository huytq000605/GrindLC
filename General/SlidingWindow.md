# Sliding Window & Subarray Patterns

Three related patterns for problems over subarrays/substrings.

## Pattern 1: Running Min/Max in a Sliding Window

**Idea:** Maintain the maximum and minimum value of the current sliding window using a **monotonic deque**, so each can be queried in O(1) amortized as the window slides.

### Examples
In Sliding Window:
- Maximum Sliding Window
- Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

## Pattern 2: Subarray Value Based on Min/Max in a Range

**Idea:** Use a **prefix sum** for range sums, plus a **monotonic stack** to locate boundaries for each element.

Use the monotonic stack to find, for each element:
- the next nearest greater/smaller element, and
- the previous nearest greater/smaller element.

Then compute the contribution for each element.

### Examples
In Stack/Queue:
- Maximum Subarray Min-Product
- Largest Rectangle in Histogram

## Pattern 3: Count Subarrays With Exactly X Elements and At Least Y Elements

**Idea:** "Exactly X" is hard to count directly, so count "at least" and subtract. When a problem also requires a second condition (at least Y elements of another property), fold that condition into the same helper.

- Write a helper `f` that counts how many subarrays have **at least** X elements **and** at least Y elements (of the properties in question).
- The number of subarrays with **exactly** X (while still satisfying the at-least-Y condition) is then `f(x) - f(x+1)`.

### Examples
- Count of Substrings Containing Every Vowel and K Consonants II (every vowel **at least** once = the Y dimension, **exactly** k consonants = the X dimension)
