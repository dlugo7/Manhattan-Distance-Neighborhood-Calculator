"""
Manhattan Distance Neighborhood Calculator - GUI Demo
====================================================

Visual demonstration of the Manhattan distance neighborhood calculation.

Run: python gui_demo.py

Author: Daniel Lugo
Date: July 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.colors import ListedColormap
import numpy as np
from typing import List, Dict, Any, Tuple
from collections import deque
import time
import random


class NeighborhoodCalculator:
    """Core algorithm for Manhattan distance neighborhood calculation"""
    
    def calculate_manhattan_neighborhood(self, grid: List[List[int]], n: int) -> Dict[str, Any]:
        """Calculate Manhattan distance neighborhood"""
        start_time = time.time()
        
        # Find positive cells
        positive_cells = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] > 0:
                    positive_cells.append((row, col))
        
        if not positive_cells:
            return {
                'count': 0,
                'neighborhood_cells': set(),
                'positive_cells': [],
                'computation_time': time.time() - start_time
            }
        
        # Calculate neighborhoods
        all_neighborhoods = set()
        grid_height = len(grid)
        grid_width = len(grid[0])
        
        for pos_row, pos_col in positive_cells:
            for distance in range(n + 1):
                for row_offset in range(-distance, distance + 1):
                    remaining_distance = distance - abs(row_offset)
                    for col_offset in range(-remaining_distance, remaining_distance + 1):
                        new_row = pos_row + row_offset
                        new_col = pos_col + col_offset
                        
                        if 0 <= new_row < grid_height and 0 <= new_col < grid_width:
                            all_neighborhoods.add((new_row, new_col))
        
        return {
            'count': len(all_neighborhoods),
            'neighborhood_cells': all_neighborhoods,
            'positive_cells': positive_cells,
            'computation_time': time.time() - start_time
        }

    def bfs_manhattan_neighborhood(self, grid: List[List[int]], n: int) -> Dict[str, Any]:
        """
        BFS-based method to calculate Manhattan neighborhood of all positive cells.

        Returns:
            Dictionary containing:
                - count: number of unique cells within distance
                - neighborhood_cells: set of (row, col) positions in the neighborhood
                - positive_cells: list of (row, col) of positive value cells
                - computation_time: runtime in seconds
        """
        start_time = time.time()

        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        positive_cells = []

        # Seed the queue with all positive cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    visited.add((r, c))
                    queue.append(((r, c), 0))
                    positive_cells.append((r, c))

        if not positive_cells:
            return {
                'count': 0,
                'neighborhood_cells': set(),
                'positive_cells': [],
                'computation_time': time.time() - start_time
            }

        # Perform BFS to find all reachable cells within distance n
        while queue:
            (r, c), dist = queue.popleft()
            if dist == n:
                continue

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))

        return {
            'count': len(visited),
            'neighborhood_cells': visited,
            'positive_cells': positive_cells,
            'computation_time': time.time() - start_time
        }


class NeighborhoodGUI:
    """GUI for Manhattan Distance Neighborhood Calculator"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Manhattan Distance Neighborhood Calculator - Visual Demo")
        self.root.geometry("1200x800")
        
        # Dark theme colors
        self.colors = {
            'primary': '#1a1a1a',
            'secondary': '#2d3748',
            'accent': '#4a90e2',
            'success': '#48bb78',
            'warning': '#ed8936',
            'background': '#2d3748',
            'card': '#1a202c',
            'text': '#ffffff',
            'muted': '#cbd5e0',
            'border': '#4a5568'
        }
        
        self.root.configure(bg=self.colors['background'])
        
        # Initialize calculator
        self.calculator = NeighborhoodCalculator()
        
        # Current example index
        self.current_example = 0
        self.examples_data = []
        
        # Toggle grid state
        self.show_grid = tk.BooleanVar(value=False)
        
        # Create the interface
        self.create_styles()
        self.create_layout()
        self.load_examples()
        self.display_current_example()
        
        # Bind keyboard shortcuts
        self.root.bind('<Left>', lambda e: self.previous_example())
        self.root.bind('<Right>', lambda e: self.next_example())
        self.root.bind('<Control-s>', lambda e: self.save_image())
        self.root.bind('<Control-n>', lambda e: self.open_custom_grid())
        
        # Make window resizable
        self.root.minsize(1000, 700)
        self.root.focus_set()
        
    def create_styles(self):
        style = ttk.Style()
        
        try:
            style.theme_use('clam')
        except:
            pass
        
        # Button styling
        style.configure('Dark.TButton',
                       background=self.colors['secondary'],
                       foreground=self.colors['text'],
                       borderwidth=1,
                       focuscolor='none',
                       padding=(20, 10),
                       relief='flat',
                       font=('Helvetica', 10, 'bold'))
        
        style.map('Dark.TButton',
                 background=[('active', self.colors['accent']),
                            ('pressed', self.colors['primary'])],
                 foreground=[('active', self.colors['text']),
                            ('pressed', self.colors['text'])])
        
        # Label styling
        style.configure('Title.TLabel',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 16, 'bold'))
        
        style.configure('Info.TLabel',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 12))
        
        # Other components
        style.configure('Dark.TCheckbutton',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       focuscolor='none',
                       font=('Helvetica', 11, 'bold'))
        
        style.configure('Dark.TRadiobutton',
                       background=self.colors['card'],
                       foreground=self.colors['text'],
                       focuscolor='none',
                       font=('Helvetica', 11, 'bold'))
        
        style.configure('Dark.TEntry',
                       fieldbackground=self.colors['secondary'],
                       foreground=self.colors['text'],
                       borderwidth=2,
                       relief='flat',
                       font=('Helvetica', 11, 'bold'),
                       insertcolor=self.colors['text'])
        
        style.configure('Card.TFrame',
                       background=self.colors['card'],
                       relief='flat')
    
    def create_layout(self):
        """Create the interface layout"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame, style='Card.TFrame')
        header_frame.pack(fill='x', pady=(0, 20))
        
        ttk.Label(header_frame, text="Manhattan Distance Neighborhood Calculator",
                 style='Title.TLabel').pack(pady=20)
        
        # Controls
        control_frame = ttk.Frame(main_frame, style='Card.TFrame')
        control_frame.pack(fill='x', pady=(0, 20))
        
        # Navigation
        nav_frame = tk.Frame(control_frame, bg=self.colors['card'])
        nav_frame.pack(pady=15)
        
        self.prev_button = ttk.Button(nav_frame, text="◀ Previous", 
                                     style='Dark.TButton',
                                     command=self.previous_example)
        self.prev_button.pack(side='left', padx=10)
        
        self.example_info = ttk.Label(nav_frame, text="Example 1 of 5",
                                     style='Info.TLabel')
        self.example_info.pack(side='left', padx=20)
        
        self.next_button = ttk.Button(nav_frame, text="Next ▶",
                                     style='Dark.TButton',
                                     command=self.next_example)
        self.next_button.pack(side='left', padx=10)
        
        ttk.Button(nav_frame, text="Save Image", style='Dark.TButton',
                  command=self.save_image).pack(side='left', padx=10)
        
        # Settings
        settings_frame = tk.Frame(control_frame, bg=self.colors['card'])
        settings_frame.pack(pady=(0, 15))
        
        # Color scheme
        scheme_frame = tk.Frame(settings_frame, bg=self.colors['card'])
        scheme_frame.pack(side='left', padx=20)
        
        ttk.Label(scheme_frame, text="Color Scheme:", style='Info.TLabel').pack(anchor='w')
        self.color_scheme_var = tk.StringVar(value='default')
        
        for scheme in ['default', 'high_contrast', 'blue_theme', 'green_theme']:
            ttk.Radiobutton(scheme_frame, text=scheme.replace('_', ' ').title(),
                           variable=self.color_scheme_var, value=scheme,
                           style='Dark.TRadiobutton',
                           command=self.display_current_example).pack(anchor='w')
        
        # N value
        n_frame = tk.Frame(settings_frame, bg=self.colors['card'])
        n_frame.pack(side='left', padx=20)
        
        ttk.Label(n_frame, text="Manhattan Distance (N):", style='Info.TLabel').pack(anchor='w')
        
        n_control = tk.Frame(n_frame, bg=self.colors['card'])
        n_control.pack(anchor='w')
        
        self.n_var = tk.StringVar(value='2')
        self.n_entry = ttk.Entry(n_control, textvariable=self.n_var, width=5, style='Dark.TEntry')
        self.n_entry.pack(side='left', padx=5)
        self.n_entry.bind('<Return>', self.update_n_value)
        
        ttk.Button(n_control, text="Update", style='Dark.TButton',
                  command=self.update_n_value).pack(side='left', padx=5)
        
        # Custom grid
        custom_frame = tk.Frame(settings_frame, bg=self.colors['card'])
        custom_frame.pack(side='left', padx=20)
        
        ttk.Label(custom_frame, text="Custom Grid:", style='Info.TLabel').pack(anchor='w')
        ttk.Button(custom_frame, text="Create Custom Grid", style='Dark.TButton',
                  command=self.open_custom_grid).pack(anchor='w', pady=5)
        
        # Display options
        display_frame = tk.Frame(settings_frame, bg=self.colors['card'])
        display_frame.pack(side='left', padx=20)
        
        ttk.Label(display_frame, text="Display Options:", style='Info.TLabel').pack(anchor='w')
        ttk.Checkbutton(display_frame, text="Show Grid Lines", variable=self.show_grid,
                       style='Dark.TCheckbutton', command=self.display_current_example).pack(anchor='w')
        
        # Visualization
        content_frame = ttk.Frame(main_frame, style='Card.TFrame')
        content_frame.pack(fill='both', expand=True)
        
        viz_panel = tk.Frame(content_frame, bg=self.colors['card'])
        viz_panel.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(12, 8), facecolor=self.colors['card'])
        self.fig.patch.set_facecolor(self.colors['card'])
        self.ax.set_facecolor(self.colors['card'])
        
        self.canvas = FigureCanvasTkAgg(self.fig, viz_panel)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        self.canvas.get_tk_widget().configure(bg=self.colors['card'])
        self.canvas.get_tk_widget().focus_set()
    
    def load_examples(self):
        """Load demonstration examples"""
        self.examples_data = [
            {
                'title': 'Basic Example',
                'description': 'Two positive cells with overlapping neighborhoods',
                'grid': [
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0]
                ],
                'n': 2
            },
            {
                'title': 'Edge Cases',
                'description': 'Positive cells at boundaries',
                'grid': [
                    [1, 0, 0, 0, 2],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [3, 0, 0, 0, 4]
                ],
                'n': 3
            },
            {
                'title': 'Complex Pattern',
                'description': 'Multiple overlapping neighborhoods',
                'grid': [
                    [0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                ],
                'n': 2
            },
            {
                'title': 'Dense Grid',
                'description': 'Many positive cells',
                'grid': [
                    [1, 0, 2, 0, 1],
                    [0, 0, 0, 0, 0],
                    [3, 0, 0, 0, 4],
                    [0, 0, 0, 0, 0],
                    [2, 0, 1, 0, 3]
                ],
                'n': 1
            },
            {
                'title': 'Large Scale',
                'description': 'Performance test with larger grid',
                'grid': [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                ],
                'n': 4
            }
        ]
    
    def get_color_scheme(self, scheme_name: str) -> Dict[str, str]:
        """Get color scheme for visualization"""
        schemes = {
            'default': {'empty': '#f7fafc', 'neighborhood': '#cbd5e0', 'positive': '#1a202c'},
            'high_contrast': {'empty': '#ffffff', 'neighborhood': '#808080', 'positive': '#000000'},
            'blue_theme': {'empty': '#ebf8ff', 'neighborhood': '#bee3f8', 'positive': '#1e40af'},
            'green_theme': {'empty': '#f0fff4', 'neighborhood': '#c6f6d5', 'positive': '#166534'}
        }
        return schemes.get(scheme_name, schemes['default'])
    
    def display_current_example(self):
        """Display current example with visualization"""
        if not self.examples_data:
            return
        
        example = self.examples_data[self.current_example]
        current_n = int(self.n_var.get())
        
        # Calculate result
        result = self.calculator.bfs_manhattan_neighborhood(example['grid'], current_n)
        # result = self.calculator.calculate_manhattan_neighborhood(example['grid'], current_n)
        example['result'] = result
        example['n'] = current_n
        
        # Clear plot
        self.ax.clear()
        
        # Get colors
        colors = self.get_color_scheme(self.color_scheme_var.get())
        
        # Create display grid
        grid = np.array(example['grid'])
        display_grid = np.zeros_like(grid, dtype=int)
        
        # Mark neighborhoods and positive cells
        for cell in result['neighborhood_cells']:
            display_grid[cell[0], cell[1]] = 1
        for cell in result['positive_cells']:
            display_grid[cell[0], cell[1]] = 2
        
        # Create visualization
        cmap = ListedColormap([colors['empty'], colors['neighborhood'], colors['positive']])
        bounds = [0, 1, 2, 3]
        norm = plt.matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        
        self.ax.imshow(display_grid, cmap=cmap, norm=norm, aspect='equal')
        
        # Add cell values
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i, j] > 0:
                    text_color = 'white' if colors['positive'] in ['#1a202c', '#000000', '#1e40af', '#166534'] else 'black'
                    self.ax.text(j, i, str(grid[i, j]), ha='center', va='center',
                               fontsize=16, fontweight='bold', color=text_color)
        
        # Add grid lines if enabled
        if self.show_grid.get():
            for i in range(len(grid) + 1):
                self.ax.axhline(y=i - 0.5, color='white', linewidth=1, alpha=0.7)
            for j in range(len(grid[0]) + 1):
                self.ax.axvline(x=j - 0.5, color='white', linewidth=1, alpha=0.7)
        
        # Title
        self.ax.set_title(f"{example['title']}\nN={current_n} | Count: {result['count']} | Time: {result['computation_time']:.4f}s",
                          fontsize=14, fontweight='bold', pad=20, color=self.colors['text'])
        
        # Legend
        legend_elements = [
            plt.Rectangle((0, 0), 1, 1, facecolor=colors['empty'], edgecolor='black', label='Empty'),
            plt.Rectangle((0, 0), 1, 1, facecolor=colors['neighborhood'], edgecolor='black', label='Neighborhood'),
            plt.Rectangle((0, 0), 1, 1, facecolor=colors['positive'], edgecolor='white', label='Positive Cell')
        ]
        legend = self.ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.6, 1))
        legend.get_frame().set_facecolor(self.colors['card'])
        for text in legend.get_texts():
            text.set_color(self.colors['text'])
        
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        # Update display
        self.canvas.draw()
        self.example_info.configure(text=f"Example {self.current_example + 1} of {len(self.examples_data)}")
        self.n_var.set(str(current_n))
    
    def previous_example(self):
        """Navigate to previous example"""
        if self.current_example > 0:
            self.current_example -= 1
            self.display_current_example()
    
    def next_example(self):
        """Navigate to next example"""
        if self.current_example < len(self.examples_data) - 1:
            self.current_example += 1
            self.display_current_example()
    
    def update_n_value(self, event=None):
        """Update N value and recalculate"""
        try:
            new_n = int(self.n_var.get())
            if new_n >= 0:
                self.display_current_example()
            else:
                messagebox.showerror("Invalid Input", "N must be non-negative")
                self.n_var.set(str(self.examples_data[self.current_example]['n']))
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
            self.n_var.set(str(self.examples_data[self.current_example]['n']))
    
    def open_custom_grid(self):
        """Open custom grid creator"""
        CustomGridDialog(self.root, self)
    
    def save_image(self):
        """Save current visualization"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("PDF files", "*.pdf")],
            title="Save Visualization"
        )
        if filename:
            try:
                self.fig.savefig(filename, dpi=300, bbox_inches='tight')
                messagebox.showinfo("Success", f"Image saved to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {e}")


class CustomGridDialog:
    """Dialog for creating custom grids"""
    
    def __init__(self, parent, main_app):
        self.parent = parent
        self.main_app = main_app
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Create Custom Grid")
        self.dialog.geometry("800x600")
        self.dialog.configure(bg=main_app.colors['background'])
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.rows_var = tk.StringVar(value='5')
        self.cols_var = tk.StringVar(value='5')
        self.grid_data = []
        self.grid_entries = []
        
        self.create_interface()
        self.create_grid(5, 5)
        
        # Center dialog
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (400)
        y = (self.dialog.winfo_screenheight() // 2) - (300)
        self.dialog.geometry(f"800x600+{x}+{y}")
    
    def create_interface(self):
        """Create the custom grid interface"""
        main_frame = tk.Frame(self.dialog, bg=self.main_app.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header
        header = tk.Frame(main_frame, bg=self.main_app.colors['card'])
        header.pack(fill='x', pady=(0, 15))
        
        tk.Label(header, text="Custom Grid Creator", font=('Helvetica', 16, 'bold'),
                bg=self.main_app.colors['card'], fg=self.main_app.colors['text']).pack(pady=15)
        
        # Size controls
        size_frame = tk.Frame(main_frame, bg=self.main_app.colors['card'])
        size_frame.pack(fill='x', pady=(0, 15))
        
        size_controls = tk.Frame(size_frame, bg=self.main_app.colors['card'])
        size_controls.pack(pady=15)
        
        tk.Label(size_controls, text="Grid Size:", font=('Helvetica', 12, 'bold'),
                bg=self.main_app.colors['card'], fg=self.main_app.colors['text']).pack(side='left', padx=10)
        
        tk.Label(size_controls, text="Rows:", bg=self.main_app.colors['card'], 
                fg=self.main_app.colors['text']).pack(side='left', padx=5)
        
        self.rows_entry = tk.Entry(size_controls, textvariable=self.rows_var, width=5,
                                  bg=self.main_app.colors['secondary'], fg=self.main_app.colors['text'])
        self.rows_entry.pack(side='left', padx=5)
        
        tk.Label(size_controls, text="Cols:", bg=self.main_app.colors['card'], 
                fg=self.main_app.colors['text']).pack(side='left', padx=5)
        
        self.cols_entry = tk.Entry(size_controls, textvariable=self.cols_var, width=5,
                                  bg=self.main_app.colors['secondary'], fg=self.main_app.colors['text'])
        self.cols_entry.pack(side='left', padx=5)
        
        tk.Button(size_controls, text="Update Grid", command=self.update_grid_size,
                 bg=self.main_app.colors['accent'], fg='white', font=('Helvetica', 10, 'bold')).pack(side='left', padx=10)
        
        # Grid frame
        self.grid_frame = tk.Frame(main_frame, bg=self.main_app.colors['card'])
        self.grid_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        # Buttons
        button_frame = tk.Frame(main_frame, bg=self.main_app.colors['background'])
        button_frame.pack(fill='x', side='bottom')
        
        tk.Button(button_frame, text="Random Grid", command=self.random_grid,
                 bg=self.main_app.colors['success'], fg='white', font=('Helvetica', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="Clear Grid", command=self.clear_grid,
                 bg=self.main_app.colors['warning'], fg='white', font=('Helvetica', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="Cancel", command=self.dialog.destroy,
                 bg=self.main_app.colors['secondary'], fg='white', font=('Helvetica', 10, 'bold')).pack(side='right', padx=5)
        
        tk.Button(button_frame, text="Create Example", command=self.create_example,
                 bg=self.main_app.colors['accent'], fg='white', font=('Helvetica', 10, 'bold')).pack(side='right', padx=5)
    
    def create_grid(self, rows, cols):
        """Create the grid input interface"""
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        self.grid_data = [[0 for _ in range(cols)] for _ in range(rows)]
        self.grid_entries = []
        
        container = tk.Frame(self.grid_frame, bg=self.main_app.colors['card'])
        container.pack(expand=True, fill='both', pady=10)
        
        cell_width = max(3, min(6, 40 // cols))
        
        for r in range(rows):
            row_entries = []
            row_frame = tk.Frame(container, bg=self.main_app.colors['card'])
            row_frame.pack()
            
            for c in range(cols):
                entry = tk.Entry(row_frame, width=cell_width, justify='center',
                               bg=self.main_app.colors['secondary'], fg=self.main_app.colors['text'])
                entry.pack(side='left', padx=1, pady=1)
                entry.insert(0, '0')
                entry.bind('<FocusOut>', lambda e, r=r, c=c: self.update_cell(r, c, e.widget.get()))
                row_entries.append(entry)
            
            self.grid_entries.append(row_entries)
    
    def update_grid_size(self):
        """Update grid size"""
        try:
            rows = int(self.rows_var.get())
            cols = int(self.cols_var.get())
            if 1 <= rows <= 20 and 1 <= cols <= 20:
                self.create_grid(rows, cols)
            else:
                messagebox.showerror("Invalid Size", "Grid size must be between 1×1 and 20×20")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    
    def update_cell(self, row, col, value):
        """Update cell value"""
        try:
            self.grid_data[row][col] = int(value) if value else 0
        except ValueError:
            self.grid_entries[row][col].delete(0, tk.END)
            self.grid_entries[row][col].insert(0, '0')
            self.grid_data[row][col] = 0
    
    def random_grid(self):
        """Fill grid with random values"""
        for r in range(len(self.grid_data)):
            for c in range(len(self.grid_data[0])):
                value = random.choice([0, 0, 0, 1, 2, 3])  # Mostly zeros
                self.grid_data[r][c] = value
                self.grid_entries[r][c].delete(0, tk.END)
                self.grid_entries[r][c].insert(0, str(value))
    
    def clear_grid(self):
        """Clear all grid values"""
        for r in range(len(self.grid_data)):
            for c in range(len(self.grid_data[0])):
                self.grid_data[r][c] = 0
                self.grid_entries[r][c].delete(0, tk.END)
                self.grid_entries[r][c].insert(0, '0')
    
    def create_example(self):
        """Create new example from custom grid"""
        try:
            n_value = int(self.main_app.n_var.get())
            result = self.main_app.calculator.calculate_manhattan_neighborhood(self.grid_data, n_value)
            
            new_example = {
                'title': f'Custom Grid {len(self.main_app.examples_data) + 1}',
                'description': f'User-created {len(self.grid_data)}×{len(self.grid_data[0])} grid',
                'grid': [row[:] for row in self.grid_data],
                'n': n_value,
                'result': result
            }
            
            self.main_app.examples_data.append(new_example)
            self.main_app.current_example = len(self.main_app.examples_data) - 1
            self.main_app.display_current_example()
            
            self.dialog.destroy()
            messagebox.showinfo("Success", f"Custom grid created! Now showing example {len(self.main_app.examples_data)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create example: {e}")


def main():
    root = tk.Tk()
    app = NeighborhoodGUI(root)
    
    def on_closing():
        root.quit()
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main() 