# Array Index Math (2D Grid Traversal)

**Idea:** Handy index formulas for traversing a 2D grid, working with its diagonals and sub-squares, and converting between 2D and flat 1D representations.

## Notation

- **rows** — number of rows
- **cols** — number of columns
- **row** — current row
- **col** — current column

## Useful Formulas

- **Move down one row, same column** (`col -> col`): `pos = currentPos + cols`.
- **Diagonals:** there are 2 families of diagonals, identified by `row + col` and by `row - col`.
- **Square index in a square matrix** (sub-square edge length = **edge**): `idxSquare = (row // edge) * edge + (col // edge)`.

## 2D <-> 1D Conversion

- **2D -> 1D:** `id = row * cols + col`
- **1D -> 2D:** `row = id // cols`, `col = id % cols`
