# Array traverse
## Number of row = **rows**
## Number of col = **cols**
## Current row = **row**
## Current col = **col**

## Go to next row with column = column + 1: pos = currentPos + cols
## There are 2 Diagonals: defined by row + col, row - col
## Square (edge = **edge**) index in Square Matrix: idxSquare = (row // edge) * edge + (col // edge)

## 2D <-> 1D: 
### 2D -> 1D: id = row * cols + col
### 1D -> 2D: row = id // cols, col = id % cols
