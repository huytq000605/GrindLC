# Straight Line Equation from Two Points

**Idea:** Given two points on a line, build the line's direction vector, rotate it 90° to get a normal vector `(a, b)`, then solve for `c` by plugging one point into `ax + by + c = 0`.

## Steps

Given two points `(x1, y1)` and `(x2, y2)` on the line:

1. **Direction vector:** `(vx, vy) = (x2 - x1, y2 - y1)`
2. **Normal vector:** `(nvx, nvy) = (vy, -vx)`
3. **Equation:** `ax + by + c = 0` with `a = nvx`, `b = nvy`
4. **Solve for `c`:** substitute `x = x1`, `y = y1`, giving `c = -ax - by = -nvx*x1 - nvy*y1`
