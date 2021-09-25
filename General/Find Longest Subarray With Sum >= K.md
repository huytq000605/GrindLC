# Find Longest Subarray with Sum >= K

## Using Prefix Sum && Monotonous Stack

## Example
	- 962. Maximum Width Ramp
	- 862. Shortest Subarray with Sum at Least K
	- 1124. Longest Well-Performing Interval

First we need to calculate prefix Sum to look up sum of a range in O(1)

We first loop through prefix array with a monotonous stack to save starting position

We use monotonous stack because the next element can only be a valid start if prefix at that position is **strictly smaller** the top of the stack (or if the stack is empty)