import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import time

# Define a class for a binary tree node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define a class for the binary tree
class BinaryTree:
    def _init_(self):
        self.root = None

    # Function to insert a node into the binary tree
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)

    # Function to perform inorder traversal
    def inorder_traversal(self, node, visit):
        if node:
            self.inorder_traversal(node.left, visit)
            visit(node)
            self.inorder_traversal(node.right, visit)

    # Function to perform postorder traversal
    def postorder_traversal(self, node, visit):
        if node:
            self.postorder_traversal(node.left, visit)
            self.postorder_traversal(node.right, visit)
            visit(node)

    # Function to perform preorder traversal
    def preorder_traversal(self, node, visit):
        if node:
            visit(node)
            self.preorder_traversal(node.left, visit)
            self.preorder_traversal(node.right, visit)

# Define the GUI class
class BinaryTreeVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Binary Tree Visualizer")

        self.canvas = tk.Canvas(master, width=800, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.binary_tree = BinaryTree()
        self.node_elements = {}  # Dictionary to store node elements
        self.traversal_index = 0

        # Add label for array input
        self.entry_label = tk.Label(master, text="Enter array (comma-separated):", font=("Arial", 12))
        self.entry_label.pack(pady=10)

        # Add styled entry widget for array input
        self.entry = tk.Entry(master, font=("Arial", 12), bd=2, relief="solid")
        self.entry.pack(pady=5, padx=10, ipady=5, fill=tk.BOTH, expand=True)

        # Add styled button to submit array
        self.submit_button = tk.Button(master, text="Submit", font=("Arial", 12), command=self.submit_array, bg="blue", fg="white", bd=2, relief="raised")
        self.submit_button.pack(pady=5)

        # Add label for traversal selection
        self.traversal_label = tk.Label(master, text="Select traversal:", font=("Arial", 12))
        self.traversal_label.pack(pady=10)

        # Create a themed style for the dropdown menu
        self.style = ThemedStyle(master)
        self.style.theme_use('clam')  # Choose the theme (options: 'alt', 'clam', 'classic', 'default', 'vista', 'xpnative')

        # Add a dropdown menu for traversal options
        self.traversal_var = tk.StringVar()
        self.traversal_var.set("Inorder")  # Default to Inorder traversal
        self.traversal_menu = ttk.Combobox(master, textvariable=self.traversal_var, values=["Inorder", "Preorder", "Postorder"], state="readonly")
        self.traversal_menu.pack()

        # Add label for traversal order
        self.order_label = tk.Label(master, text="Traversal Order:", font=("Arial", 12))
        self.order_label.pack(pady=10)

        # Add listbox for traversal order
        self.traversal_order = tk.Listbox(master, font=("Arial", 12), bd=2, relief="solid", width=50, height=1, bg="lightgray", fg="blue", selectbackground="gray", selectforeground="white")
        self.traversal_order.pack(pady=5)

    def insert_element(self, value):
        self.binary_tree.insert(value)
        self.update_tree()

    def update_tree(self):
        self.canvas.delete("all")
        self.node_elements.clear()  # Clear the dictionary
        self.draw_tree(self.binary_tree.root, 400, 50, 200)

    def draw_tree(self, node, x, y, spacing):
        if node:
            self.draw_tree(node.left, x - spacing, y + 50, spacing // 2)
            node_id = self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="black")
            self.node_elements[node.value] = node_id  # Store node element in the dictionary
            self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 12, "bold"))
            if node.left:
                left_index = len(self.node_elements) - 1
                self.canvas.create_line(x, y, x - spacing, y + 50)
            if node.right:
                right_index = len(self.node_elements) - 1
                self.canvas.create_line(x, y, x + spacing, y + 50)
            self.draw_tree(node.right, x + spacing, y + 50, spacing // 2)

    def animate_traversal(self):
        traversal_mode = self.traversal_var.get()
        self.traversal_index = 0
        self.inorder_nodes = []
        if traversal_mode == "Inorder":
            self.binary_tree.inorder_traversal(self.binary_tree.root, self.collect_nodes)
        elif traversal_mode == "Preorder":
            self.binary_tree.preorder_traversal(self.binary_tree.root, self.collect_nodes)
        elif traversal_mode == "Postorder":
            self.binary_tree.postorder_traversal(self.binary_tree.root, self.collect_nodes)
        self.highlight_node()

    def collect_nodes(self, node):
        self.inorder_nodes.append(node)
        current_content = self.traversal_order.get(0, tk.END)
        new_content = ' '.join(current_content) + str(node.value) + " "
        self.traversal_order.delete(0, tk.END)  # Clear the listbox
        self.traversal_order.insert(tk.END, new_content)  # Insert updated content

    def highlight_node(self):
        if self.traversal_index < len(self.inorder_nodes):
            node = self.inorder_nodes[self.traversal_index]
            if node.value in self.node_elements:  # Check if node value exists in the dictionary
                self.canvas.itemconfig(self.node_elements[node.value], fill="yellow")
                self.master.update()
                time.sleep(1)  # Adjust the animation speed here (in seconds)
                self.canvas.itemconfig(self.node_elements[node.value], fill="lightblue")
                self.traversal_index += 1
                self.master.after(1000, self.highlight_node)

    def submit_array(self):
        array = self.entry.get().split(",")
        for element in array:
            try:
                value = int(element.strip())
                self.insert_element(value)
            except ValueError:
                print("Invalid input:", element.strip())
        self.animate_traversal()


# Create the main GUI window
root = tk.Tk()
app = BinaryTreeVisualizer(root)
root.mainloop()
