# Island Perimeter

This Python project calculates the perimeter of an island described in a grid. The grid consists of cells representing land (1) and water (0). The goal is to find the perimeter of the island, considering the following rules:

- Each cell is square, with a side length of 1.
- Cells are connected horizontally or vertically (not diagonally).
- The grid is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

## Usage

To use the `island_perimeter` function, follow these steps:

1. Import the function:
   ```python
   from island_perimeter import island_perimeter
   ```

2. Create a grid (list of lists) representing the island. For example:
   ```python
   grid = [
       [0, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0]
   ]
   ```

3. Call the function with the grid as an argument:
   ```python
   perimeter = island_perimeter(grid)
   print(f"The perimeter of the island is: {perimeter}")
   ```

## Example

For the given grid:
```
0 1 0 0
1 1 1 0
0 1 0 0
1 1 0 0
```

The perimeter of the island is 16.

## Implementation

The `island_perimeter` function iterates through the grid, counting the perimeter based on adjacent land cells. It handles edge cases and ensures that the island is completely surrounded by water.

Feel free to use this project in your own Python applications! 🌴🏝️
