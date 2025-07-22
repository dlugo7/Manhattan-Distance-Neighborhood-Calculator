# Manhattan Distance Neighborhood Calculator

A clean, solution for calculating Manhattan distance neighborhoods in 2D grids. This project provides two distinct approaches.

## Project Structure and Guidelines

### 1. **Core Algorithm** (`interview_solution.py`)
- **Purpose**: Algorithm implementation with test cases
- **Run**: `python interview_solution.py`

### 2. **Visual Demonstration** (`gui_demo.py`)
- **Purpose**: Professional GUI with interactive visualization
- **Features**: Dark theme, real-time updates, custom grid creation
- **Run**: `python gui_demo.py`

## Quick Start

### Algorithm Showcase
```bash
python interview_solution.py
```

### Visual GUI Showcase
```bash
python gui_demo.py
```

## Problem

Calculate the number of unique cells within Manhattan distance N of any positive values in a 2D grid.

**Manhattan Distance Formula**: `|x1-x2| + |y1-y2|`

**Key Requirements**:
- Each cell counted only once (no duplicates)
- Positive cells count as 0-distance members
- Works with any valid grid dimensions
- Handles edge cases and boundaries

## Algorithm

Located in `interview_solution.py`:

```python
def calculate_manhattan_neighborhood(grid: List[List[int]], n: int) -> int:
    """
    Calculate unique cells within Manhattan distance N of positive cells.
    
    Time Complexity: O(P × N²) where P = positive cells
    Space Complexity: O(N²) for neighborhood storage
    """

def bfs_manhattan_neighborhood(grid: List[List[int]], n: int) -> int:
    """
    BFS-based method to calculate Manhattan neighborhood of all positive cells.
    
    Time Complexity: O(rows × cols) worst case  
    Space Complexity: O(rows × cols) for visited storage
    """

```

## Test Cases

The interview solution includes comprehensive test cases:

1. **Single Positive Cell** - Basic functionality
2. **Multiple Positive Cells** - Overlapping neighborhoods
3. **Boundary Cases** - Edge and corner positions
4. **Dense Grid** - Many positive cells
5. **Single Cell** - Minimum grid size (N=0)
6. **Large N** - N larger than grid dimensions
7. **No Positive Cells** - Empty grid handling


## Dependencies

**For Algorithm Mode** (`interview_solution.py`):
- Python 3.6+ (built-in modules only)

**For GUI Mode** (`gui_demo.py`):
```bash
pip install numpy matplotlib
```
Note: `tkinter` usually comes with Python

## Usage Examples

### Algorithm Mode Output
```
============================================================
TEST CASE: Single Positive Cell (N=2)
============================================================

Grid:
-----------------
|  0 |  0 |  0 |
-----------------
|  0 |  1 |  0 |
-----------------
|  0 |  0 |  0 |
-----------------

Positive cells: [(1, 1)]
Manhattan distance N: 2

RESULT: 13 cells in neighborhood
Computation time: 0.145ms
Expected: 13 | Got: 13 | ✅ PASS
```

Thanks!
- Daniel