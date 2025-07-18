#!/usr/bin/env python3
"""
Manhattan Distance Neighborhood Calculator
==========================================

Interview Solution: Core Algorithm Implementation

This file contains the complete solution to the Manhattan distance neighborhood
calculation problem as specified in the coding challenge PDF.

Problem: Calculate the number of cells within Manhattan distance N of any
positive values in a 2D grid.

Author: Interview Candidate
Date: 2024
"""

from typing import List, Set, Tuple
import time


def find_positive_cells(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Find all cells containing positive values"""
    positive_cells = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 0:
                positive_cells.append((row, col))
    return positive_cells


def calculate_manhattan_neighborhood(grid: List[List[int]], n: int) -> int:
    """
    Calculate the number of unique cells within Manhattan distance N of any positive cell.
    
    Args:
        grid: 2D list representing the grid
        n: Manhattan distance threshold (N >= 0)
    
    Returns:
        Number of unique cells in the neighborhood
    """
    if not grid or not grid[0]:
        return 0
    
    if n < 0:
        return 0
    
    # Find all positive cells
    positive_cells = find_positive_cells(grid)
    
    if not positive_cells:
        return 0
    
    # Calculate neighborhood for all positive cells
    all_neighborhoods = set()
    grid_height = len(grid)
    grid_width = len(grid[0])
    
    for pos_row, pos_col in positive_cells:
        # For each positive cell, find all cells within Manhattan distance N
        for distance in range(n + 1):
            for row_offset in range(-distance, distance + 1):
                remaining_distance = distance - abs(row_offset)
                for col_offset in range(-remaining_distance, remaining_distance + 1):
                    new_row = pos_row + row_offset
                    new_col = pos_col + col_offset
                    
                    # Check bounds
                    if 0 <= new_row < grid_height and 0 <= new_col < grid_width:
                        all_neighborhoods.add((new_row, new_col))
    
    return len(all_neighborhoods)


def print_grid(grid: List[List[int]], title: str = "Grid"):
    """Print a formatted grid for visualization"""
    print(f"\n{title}:")
    print("-" * (len(grid[0]) * 4 + 1))
    for row in grid:
        print("|", end="")
        for cell in row:
            print(f" {cell:2d} ", end="|")
        print()
    print("-" * (len(grid[0]) * 4 + 1))


def run_test_case(test_name: str, grid: List[List[int]], n: int, expected: int = None):
    """Run a single test case and display results"""
    print(f"\n{'='*60}")
    print(f"TEST CASE: {test_name}")
    print(f"{'='*60}")
    
    # Display the grid
    print_grid(grid)
    
    # Find positive cells
    positive_cells = find_positive_cells(grid)
    print(f"\nPositive cells: {positive_cells}")
    print(f"Manhattan distance N: {n}")
    
    # Calculate result
    start_time = time.time()
    result = calculate_manhattan_neighborhood(grid, n)
    end_time = time.time()
    
    print(f"\nRESULT: {result} cells in neighborhood")
    print(f"Computation time: {(end_time - start_time)*1000:.3f}ms")
    
    # Check expected result if provided
    if expected is not None:
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Expected: {expected} | Got: {result} | {status}")
    
    return result


def main():
    """Main function demonstrating the algorithm with test cases"""
    print("Manhattan Distance Neighborhood Calculator")
    print("Interview Solution - Core Algorithm Implementation")
    print("\nProblem: Calculate unique cells within Manhattan distance N of positive values")
    print("Formula: Manhattan distance = |x1-x2| + |y1-y2|")
    
    # Test Case 1: Basic example from PDF
    print("\n" + "="*80)
    print("RUNNING TEST CASES")
    print("="*80)
    
    # Test Case 1: Single positive cell, N=2
    grid1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    run_test_case("Single Positive Cell (N=2)", grid1, 2, 12)
    
    # Test Case 2: Two positive cells with overlapping neighborhoods, N=2
    grid2 = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0]
    ]
    run_test_case("Two Positive Cells (N=2)", grid2, 2, 19)
    
    # Test Case 3: Edge case - positive cell at boundary, N=3
    grid3 = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2]
    ]
    run_test_case("Boundary Cells (N=3)", grid3, 3, 16)
    
    # Test Case 4: Multiple positive cells, N=1
    grid4 = [
        [1, 0, 2],
        [0, 0, 0],
        [3, 0, 4]
    ]
    run_test_case("Multiple Positive Cells (N=1)", grid4, 1, 8)
    
    # Test Case 5: Single cell grid, N=0
    grid5 = [[5]]
    run_test_case("Single Cell (N=0)", grid5, 0, 1)
    
    # Test Case 6: Large N value (larger than grid)
    grid6 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    run_test_case("Large N Value (N=10)", grid6, 10, 9)
    
    # Test Case 7: No positive cells
    grid7 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    run_test_case("No Positive Cells (N=2)", grid7, 2, 0)
    
    print("\n" + "="*80)
    print("ALGORITHM ANALYSIS")
    print("="*80)
    print("Time Complexity: O(P × N²) where P = number of positive cells")
    print("Space Complexity: O(N²) for storing neighborhood coordinates")
    print("Key Features:")
    print("  • Handles overlapping neighborhoods (no double counting)")
    print("  • Boundary checking for grid edges")
    print("  • Efficient set operations for duplicate removal")
    print("  • Works with any grid size and N value")
    
    print("\n" + "="*80)
    print("INTERVIEW COMPLETE")
    print("="*80)
    print("Core algorithm successfully demonstrated with multiple test cases.")
    print("Ready for technical discussion and code review.")


if __name__ == "__main__":
    main() 