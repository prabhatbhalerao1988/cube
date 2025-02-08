import tkinter as tk

# Function to draw the cube
def draw_cube(canvas, x1, y1, size):
    # Define cube vertices in 2D projection space (simplified)
    x2 = x1 + size  # Right corner
    y2 = y1  # Same horizontal line
    x3 = x1  # Same vertical line
    y3 = y1 + size  # Bottom-left corner
    x4 = x2  # Right-bottom corner
    y4 = y3  # Same as y3

    # Depth offset to simulate 3D effect
    depth_offset = 30

    # Define "far" cube vertices (projected further back)
    x1_f = x1 + depth_offset
    y1_f = y1 - depth_offset
    x2_f = x2 + depth_offset
    y2_f = y2 - depth_offset
    x3_f = x3 + depth_offset
    y3_f = y3 - depth_offset
    x4_f = x4 + depth_offset
    y4_f = y4 - depth_offset

    # Draw the front square (front face of the cube)
    canvas.create_line(x1, y1, x2, y2)
    canvas.create_line(x2, y2, x4, y4)
    canvas.create_line(x4, y4, x3, y3)
    canvas.create_line(x3, y3, x1, y1)

    # Draw the back square (back face of the cube)
    canvas.create_line(x1_f, y1_f, x2_f, y2_f)
    canvas.create_line(x2_f, y2_f, x4_f, y4_f)
    canvas.create_line(x4_f, y4_f, x3_f, y3_f)
    canvas.create_line(x3_f, y3_f, x1_f, y1_f)

    # Connect front and back squares to form cube edges
    canvas.create_line(x1, y1, x1_f, y1_f)
    canvas.create_line(x2, y2, x2_f, y2_f)
    canvas.create_line(x3, y3, x3_f, y3_f)
    canvas.create_line(x4, y4, x4_f, y4_f)

# Create the main window
root = tk.Tk()
root.title("3D Cube Simulation")

# Create the canvas for drawing
canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Draw a cube with size 100 at position (200, 150)
draw_cube(canvas, 200, 150, 100)

# Run the Tkinter event loop
root.mainloop()
