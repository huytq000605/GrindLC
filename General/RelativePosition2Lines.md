# Relative Position of Two Lines (2D Cross Product)

**Idea:** Given a shared origin `O` and two points `A`, `B`, the sign of the 2D cross product tells you the orientation of vector `OA` relative to `OB` — collinear, clockwise, or counter-clockwise.

The two direction vectors (as slopes) are:

- **OA:** `(xA - xO) / (yA - yO)`
- **OB:** `(xB - xO) / (yB - yO)`

The cross product avoids division (and division-by-zero) by cross-multiplying:

```
cross = (xA - xO) * (yB - yO) - (xB - xO) * (yA - yO)
```

## Collinear

`OA` and `OB` lie on the same line: `cross == 0`.

```
O------A---------------B
```

## OA is clockwise to OB

`cross > 0`.

```
A------O
      /
    /
  /
B
```

## OA is counter-clockwise to OB

`cross < 0`.

```
B
  \
    \
      \
        \
A--------O
```
