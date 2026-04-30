# 36. Valid Sudoku

**Difficulty:** Medium  
**Problem Link:** [LeetCode 36 - Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

## Problem Statement

Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

**Note:**

- A Sudoku board (partially filled) could be valid but not necessarily solvable.
- Only the filled cells need to be validated with the given rules.
- The board is represented as a 2D list of characters, where `'.'` indicates an empty cell.

## Examples

| Input (board)                                                                                                                                                                                                                                                                                                                                                                                             | Output  | Explanation                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------- |
| Valid board (shown below)                                                                                                                                                                                                                                                                                                                                                                                 | `true`  | No duplicate digits in any row, column, or 3×3 sub-box.              |
| `board = [["8","3",".",".","7",".",".",".","."]`<br>`["6",".",".","1","9","5",".",".","."]`<br>`[".","9","8",".",".",".",".","6","."]`<br>`["8",".",".",".","6",".",".",".","3"]`<br>`["4",".",".","8",".","3",".",".","1"]`<br>`["7",".",".",".","2",".",".",".","6"]`<br>`[".","6",".",".",".",".","2","8","."]`<br>`[".",".",".","4","1","9",".",".","5"]`<br>`[".",".",".",".","8",".",".","7","9"]]` | `false` | Duplicate `'8'` in top-left 3×3 sub-box (positions [0,0] and [3,0]). |

_(Visual representation of a valid board)_

```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

This board is valid → returns `true`.

## Approach

We need to check three constraints (rows, columns, boxes) without scanning the same cell multiple times inefficiently. A single pass through all 81 cells with three sets per region (row, column, box) ensures we can detect duplicates immediately.

### Why Sets?

- We can keep a set for each of the 9 rows, 9 columns, and 9 boxes.
- As we iterate over every cell, we check if the current digit already exists in the corresponding row‑set, column‑set, or box‑set.
- If it does → invalid board. Otherwise, we add the digit to all three sets.
- For empty cells (`'.'`), we simply skip them.

### Box Index Mapping

Each cell belongs to exactly one of the 3×3 sub‑boxes. We can calculate the box index using integer division:

```
box_index = (row // 3) * 3 + (col // 3)
```

This maps:

- Top‑left box to index 0,
- Top‑middle to 1,
- Top‑right to 2,
- Middle‑left to 3,
- … and so on up to 8.

### Algorithm Steps

1. Create three lists of 9 empty sets: `rows`, `cols`, `boxes`.
2. Loop through `r` from 0 to 8:
   - Loop through `c` from 0 to 8:
     - Let `val = board[r][c]`.
     - If `val == '.'` → continue.
     - Calculate `box_idx = (r // 3) * 3 + (c // 3)`.
     - If `val` is already in `rows[r]`, `cols[c]`, or `boxes[box_idx]` → return `False`.
     - Otherwise, add `val` to `rows[r]`, `cols[c]`, and `boxes[box_idx]`.
3. If the loops complete without finding a duplicate → return `True`.

## Complexity Analysis

- **Time Complexity:** O(1) (or O(81))  
  The board size is fixed (`9×9`). We visit each cell exactly once, and set operations are average O(1).  
  Even in the worst case, the number of operations is constant.
- **Space Complexity:** O(1)  
  We use 27 sets, each holding at most 9 digits. The total extra space is bounded by a constant (243 entries maximum).

## Code (Python)

```python
from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    # Initialize sets for rows, columns, and 3x3 sub‑boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            # Determine the index of the 3x3 box
            box_idx = (r // 3) * 3 + (c // 3)

            # Check for duplicates in current row, column, or box
            if (val in rows[r] or
                val in cols[c] or
                val in boxes[box_idx]):
                return False

            # No duplicate → record the digit
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_idx].add(val)

    return True
```

## Edge Cases

- **Empty board (all `'.'`)** → valid.
- **Partially filled but valid** → valid (the problem does not require solvability).
- **Board with duplicate digits in a row, column, or box** → invalid, detected immediately.
- **Board containing characters other than `'1'..'9'` or `'.'`** → not part of the problem's guaranteed input.

## Alternative Approaches

| Approach                                   | Time  | Space | Notes                                                                                |
| ------------------------------------------ | ----- | ----- | ------------------------------------------------------------------------------------ |
| Brute force (check each region separately) | O(9²) | O(1)  | Check each row, column, and box one by one; simpler but more code, same complexity.  |
| Bitmask / integer bits                     | O(9²) | O(1)  | Use 9 integers as bitmasks instead of sets; slightly faster, less readable.          |
| Single set of encoded tuples               | O(9²) | O(1)  | Encode `(row, digit)`, `(col, digit)`, `(box, digit)` in a single hash set; concise. |
| Three separate passes                      | O(9²) | O(1)  | Check all rows, then all columns, then all boxes; still constant time.               |

The one‑pass set approach above is clean, readable, and satisfies the constant time/space constraints perfectly.
