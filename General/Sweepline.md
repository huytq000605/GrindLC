Corporate Flight Bookings problem (In Array)
When there are array of range booking [start, end, value]
we need *value* more seats on start-th day but dont need for end-th + 1 day
we accumulate these changes => result

The linear solution relies on a "mathematical trick" (derivative?), meaning we can find the final result by computing the cumulative sum so we don't need to compute every element within the range of seats.

Let's take this example:
[[1,2,10],[2,3,20],[2,5,25]], n = 5
The first booking is [1,2,10] where 1-2 is the range, and 10 the number of seats

If you look at the code below, it becomes obvious the result array is changed to:
[10,0,-10,0,0]

Note we only changed 2 cells. This would be a huge runtime-saver if the range was 1-2000.

(There's actually an extra 0 in the result array to stay within bounds, since we mark the end of the range with -seats)

We all know after the first loop, the result array must be [10,10,0,0,0]. This is exactly what we get if we take the cumulative sum for [10,0,-10,0,0].

This is just a simple demonstration of the cumulative sum. We actually only do this at the very end of the algorithm, when we have stepped through all the bookings and marked/updated the ranges appropriately.

If we do this for all the bookings, and then apply the cumulative sum, we get this:

[10, 45, -10, -20, 0, 25, -25] -> [10, 55, 45, 25, 25, 0]

The only tricky part is paying attention to the 0-indexed result array because we added 1 for padding to mark the end of the range.

So we return only the first n elements.