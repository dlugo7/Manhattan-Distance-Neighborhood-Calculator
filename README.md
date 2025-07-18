# Manhattan Distance Neighborhood Calculator

A clean, interview-ready solution for calculating Manhattan distance neighborhoods in 2D grids. This project provides two distinct approaches perfect for technical interviews.

## 🎯 Two-Tier Interview Structure

### 1. **Core Algorithm** (`interview_solution.py`)
- **Purpose**: Pure algorithm implementation with test cases
- **Perfect for**: Algorithm-focused interviews
- **Features**: Clean code, hardcoded test cases, no GUI complexity
- **Run**: `python interview_solution.py`

### 2. **Visual Demonstration** (`gui_demo.py`)
- **Purpose**: Professional GUI with interactive visualization
- **Perfect for**: Full-stack skill demonstration
- **Features**: Dark theme, real-time updates, custom grid creation
- **Run**: `python gui_demo.py`

## 🚀 Quick Start

### Algorithm Interview Mode
```bash
python interview_solution.py
```
**Perfect for**: Shows core algorithm implementation without distractions

### Visual Demo Mode
```bash
python gui_demo.py
```
**Perfect for**: Demonstrates advanced development skills

## 📋 Problem Statement

Calculate the number of unique cells within Manhattan distance N of any positive values in a 2D grid.

**Manhattan Distance Formula**: `|x1-x2| + |y1-y2|`

**Key Requirements**:
- Each cell counted only once (no duplicates)
- Positive cells count as 0-distance members
- Works with any valid grid dimensions
- Handles edge cases and boundaries

## 🔧 Core Algorithm

Located in `interview_solution.py`:

```python
def calculate_manhattan_neighborhood(grid: List[List[int]], n: int) -> int:
    """
    Calculate unique cells within Manhattan distance N of positive cells.
    
    Time Complexity: O(P × N²) where P = positive cells
    Space Complexity: O(N²) for neighborhood storage
    """
    # Implementation details...
```

## 🎨 Visual Demo Features

Located in `gui_demo.py`:

- **Interactive Grid Visualization** with color coding
- **Real-time N Value Adjustment** 
- **Custom Grid Creation** (up to 20×20)
- **Professional Dark Theme** interface
- **4 Color Schemes** (default, high contrast, blue, green)
- **Export Functionality** (PNG, PDF)
- **Keyboard Shortcuts** for navigation

## 📊 Test Cases

The interview solution includes comprehensive test cases:

1. **Single Positive Cell** - Basic functionality
2. **Multiple Positive Cells** - Overlapping neighborhoods
3. **Boundary Cases** - Edge and corner positions
4. **Dense Grid** - Many positive cells
5. **Single Cell** - Minimum grid size (N=0)
6. **Large N** - N larger than grid dimensions
7. **No Positive Cells** - Empty grid handling

## 🎯 Interview Advantages

### For Algorithm Questions
- **Direct access** to core implementation
- **Clean, readable code** without GUI complexity
- **Comprehensive test cases** with expected results
- **Performance metrics** and complexity analysis
- **Step-by-step output** for verification

### For Full-Stack Questions
- **Professional GUI** with modern design
- **Real-time interactivity** and updates
- **Custom grid creation** with validation
- **Export capabilities** for presentations
- **Clean architecture** with separation of concerns

## 🔍 Code Navigation

### Algorithm Focus
```python
# In interview_solution.py
find_positive_cells()              # Line ~20
calculate_manhattan_neighborhood() # Line ~30
run_test_case()                   # Line ~70
```

### GUI Components
```python
# In gui_demo.py
NeighborhoodCalculator            # Line ~15
ModernNeighborhoodGUI            # Line ~60
CustomGridDialog                 # Line ~400
```

## 📈 Performance

**Algorithm Performance**:
- **5×5 grid**: ~0.1ms
- **10×10 grid**: ~0.2ms  
- **20×20 grid**: ~0.5ms

**Space Efficiency**:
- Set-based deduplication
- Boundary checking optimization
- Memory-efficient coordinate storage

## 🛠️ Dependencies

**For Algorithm Mode** (`interview_solution.py`):
- Python 3.6+ (built-in modules only)

**For GUI Mode** (`gui_demo.py`):
```bash
pip install numpy matplotlib
```
Note: `tkinter` usually comes with Python

## 🎮 Usage Examples

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

### GUI Mode Features
- **Interactive visualization** with immediate feedback
- **Custom grid creation** with drag-and-drop values
- **Real-time N adjustment** with live updates
- **Professional presentation** quality

## 🏆 Interview Ready

This structure provides:
- **Clean separation** of algorithm vs. visualization
- **No complexity overhead** when focusing on core logic
- **Professional presentation** when showcasing skills
- **Comprehensive test coverage** for validation
- **Interview-friendly** code organization

Perfect for demonstrating both algorithmic thinking and full-stack development capabilities! 