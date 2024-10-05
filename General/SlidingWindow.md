# Sliding Window

## Approach

Keep maintaining the maximum and the minimum value in a running sliding window

We wanna use a monotonous deque

## Example 
In Sliding Window:
- Maximum Sliding Window, 
- Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

# Calculate Subarray based on min/max in that range

## Approach
Use prefix sum

Use monotonous stack to:
Find next nearest greater/smaller element
Find prev nearest greater/smaller element

Calculate for each element

## Example
In Stack/Queue:
- Maximum Subarray Min-Product
- Largest Rectangle in Histogram

# Find how many subarray having exactly X elements and at least Y elements

## Approach
- Write a function to calculate how many subarrays having at least X elements and Y elements
- Now to find exact elements using f(x) - f(x+1)

## Example:
- Count of Substrings Containing Every Vowel and K Consonants II
