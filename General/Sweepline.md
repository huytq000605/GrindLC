# Sweep Line (Difference Array / Range Update with Prefix Sum)

**Idea:** Instead of touching every cell in a range update, record only the *change* at the range boundaries, then recover the final array with a single cumulative (prefix) sum at the end. This turns each range update from `O(range length)` into `O(1)`.

## 1D: Corporate Flight Bookings

(See the *Corporate Flight Bookings* problem in the **Array** section.)

Given bookings of the form `[start, end, value]`: we need `value` more seats starting on the `start`-th day, and we no longer need them from the `end + 1`-th day. We accumulate these boundary changes, and the cumulative sum gives the result.

The linear solution relies on a "mathematical trick" (think derivative / difference array): we can find the final result by computing the cumulative sum, so we never have to update every element inside the range.

### Worked example

Input: `[[1,2,10],[2,3,20],[2,5,25]]`, `n = 5`.

The first booking is `[1,2,10]`, where `1-2` is the range and `10` is the number of seats.

After applying just the first booking, the result array becomes:

```
[10, 0, -10, 0, 0]
```

Note we only changed **2 cells**. This is a huge runtime saver if the range were `1-2000`.

(There is actually an extra `0` in the result array to stay within bounds, since we mark the end of the range with `-seats`.)

We know that after the first booking the seat counts must be `[10, 10, 0, 0, 0]` — which is exactly what we get by taking the cumulative sum of `[10, 0, -10, 0, 0]`.

That is the whole idea of the cumulative sum. We only apply it **once, at the very end**, after stepping through all the bookings and marking/updating the ranges.

Doing this for all bookings and then taking the cumulative sum:

```
[10, 45, -10, -20, 0, 25, -25]  ->  [10, 55, 45, 25, 25, 0]
```

The only tricky part is paying attention to the 0-indexed result array, since we added 1 cell of padding to mark the end of each range. So we return only the first `n` elements.

## 2D: Range Update on a Grid

Apply the same technique. To add to every cell in the rectangle from `[i][j]` to `[i+H][j+W]`, update the four corners:

- `array[i][j]       += 1`
- `array[i][j+W]     -= 1`
- `array[i+H][j]     -= 1`
- `array[i+H][j+W]   += 1`

Then compute the 2D prefix sum to recover the final grid.

## Complexity

- **Time:** `O(B + n)` for 1D (`B` = number of bookings) — `O(1)` per update plus one prefix-sum pass; `O(U + H·W)` for 2D (`U` = number of rectangle updates) — `O(1)` per update plus one 2D prefix-sum pass.
- **Space:** `O(n)` for 1D, `O(H·W)` for the 2D grid.
