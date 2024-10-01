import tkinter as tk
from tkinter import messagebox, simpledialog
import collections
import heapq
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image, ImageTk
class DataStructuresGUI:
    def __init__(self, master):
        self.master = master
        self.master.title(" Data Structure Simulator: Interactive Learning Tool")
        self.master.geometry("800x600")

        # Load and set the background image
        bg_image_path = "C:/Users/Ziven/Downloads/WhatsApp Image 2024-06-18 at 9.39.52 PM.jpeg" # Update this path to your image file
        self.bg_image = Image.open(bg_image_path)
        self.bg_image = self.bg_image.resize((1500, 1000), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

        bg_label = tk.Label(self.master, image=self.bg_image_tk)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title Label with new font and color
        title_label = tk.Label(self.master, text="Data Structure Simulator: Interactive Learning Tool Introduction:", font=("Helvetica", 28, "bold"), bg="#87CEEB", fg="white")
        title_label.pack(pady=20)

        # Frame for buttons with a new layout
        button_frame = tk.Frame(self.master, bg="#4682B4")  # Change button frame color
        button_frame.pack(pady=20, padx=20, fill=tk.X)

        # Add buttons for different data structures
        buttons = [
            ("Stack", self.open_stack_window),
            ("Singly Linked List", self.open_singly_linked_list_window),
            ("Doubly Linked List", self.open_doubly_linked_list_window),
            ("Queue", self.open_queue_window),
            ("Priority Queue", self.open_priority_queue_window),
            ("Binary Tree", self.open_binary_tree_window),
            ("Huffman Coding", self.open_huffman_coding_window),
            ("BFS Graph", self.open_bfs_graph_window),
            ("DFS Graph", self.open_dfs_graph_window),
            ("Hash Table with Collision Handling", self.open_collision_hash_table_window),
            ("Abstract Data Type", self.open_adt_window),
        ]

        for i, (text, command) in enumerate(buttons):
            button = tk.Button(button_frame, text=text, font=("Helvetica", 12), width=20, height=2, command=command)
            button.grid(row=i // 2, column=i % 2, padx=10, pady=5)

    def create_tooltip(self, widget, text):
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f"+0+0")
        label = tk.Label(tooltip, text=text, background="yellow", relief="solid", borderwidth=1, font=("Arial", 12))
        label.pack(ipadx=1)
        tooltip.withdraw()

        def show_tooltip(event):
            x, y, cx, cy = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25
            tooltip.geometry(f"+{x}+{y}")
            tooltip.deiconify()

        def hide_tooltip(event):
            tooltip.withdraw()

        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)


    # Stack Implementation
    def open_stack_window(self):
        stack_window = tk.Toplevel(self.master)
        stack_window.title("Stack Implementation")
        stack_window.geometry("500x400")

        self.stack = []

        def push():
            value = simpledialog.askstring("Input", "Enter a value to push:")
            if value:
                self.stack.append(value)
                update_stack_display()

        def pop():
            if self.stack:
                self.stack.pop()
                update_stack_display()
            else:
                messagebox.showwarning("Warning", "Stack is empty!")

        def update_stack_display():
            stack_display.delete(0, tk.END)
            for item in reversed(self.stack):
                stack_display.insert(tk.END, item)

        tk.Button(stack_window, text="Push", font=("Arial", 14), command=push).pack(pady=5)
        tk.Button(stack_window, text="Pop", font=("Arial", 14), command=pop).pack(pady=5)

        stack_display = tk.Listbox(stack_window, font=("Arial", 14), height=10, width=30)
        stack_display.pack(pady=10)

    # Singly Linked List Implementation
    def open_singly_linked_list_window(self):
        singly_linked_list_window = tk.Toplevel(self.master)
        singly_linked_list_window.title("Singly Linked List Implementation")
        singly_linked_list_window.geometry("500x400")

        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        self.head = None

        def insert():
            value = simpledialog.askstring("Input", "Enter a value to insert:")
            if value:
                new_node = Node(value)
                new_node.next = self.head
                self.head = new_node
                update_display()

        def delete():
            if self.head:
                self.head = self.head.next
                update_display()
            else:
                messagebox.showwarning("Warning", "Singly Linked List is empty!")

        def update_display():
            linked_list_display.delete(0, tk.END)
            current = self.head
            while current:
                linked_list_display.insert(tk.END, current.data)
                current = current.next

        tk.Button(singly_linked_list_window, text="Insert", font=("Arial", 14), command=insert).pack(pady=5)
        tk.Button(singly_linked_list_window, text="Delete", font=("Arial", 14), command=delete).pack(pady=5)

        linked_list_display = tk.Listbox(singly_linked_list_window, font=("Arial", 14), height=10, width=30)
        linked_list_display.pack(pady=10)

    # Doubly Linked List Implementation
    def open_doubly_linked_list_window(self):
        doubly_linked_list_window = tk.Toplevel(self.master)
        doubly_linked_list_window.title("Doubly Linked List Implementation")
        doubly_linked_list_window.geometry("500x400")

        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None
                self.prev = None

        self.d_head = None

        def insert():
            value = simpledialog.askstring("Input", "Enter a value to insert:")
            if value:
                new_node = Node(value)
                new_node.next = self.d_head
                if self.d_head:
                    self.d_head.prev = new_node
                self.d_head = new_node
                update_display()

        def delete():
            if self.d_head:
                self.d_head = self.d_head.next
                if self.d_head:
                    self.d_head.prev = None
                update_display()
            else:
                messagebox.showwarning("Warning", "Doubly Linked List is empty!")

        def update_display():
            doubly_linked_list_display.delete(0, tk.END)
            current = self.d_head
            while current:
                doubly_linked_list_display.insert(tk.END, current.data)
                current = current.next

        tk.Button(doubly_linked_list_window, text="Insert", font=("Arial", 14), command=insert).pack(pady=5)
        tk.Button(doubly_linked_list_window, text="Delete", font=("Arial", 14), command=delete).pack(pady=5)

        doubly_linked_list_display = tk.Listbox(doubly_linked_list_window, font=("Arial", 14), height=10, width=30)
        doubly_linked_list_display.pack(pady=10)

    # Queue Implementation
    def open_queue_window(self):
        queue_window = tk.Toplevel(self.master)
        queue_window.title("Queue Implementation")
        queue_window.geometry("500x400")

        self.queue = collections.deque()

        def enqueue():
            value = simpledialog.askstring("Input", "Enter a value to enqueue:")
            if value:
                self.queue.append(value)
                update_queue_display()

        def dequeue():
            if self.queue:
                self.queue.popleft()
                update_queue_display()
            else:
                messagebox.showwarning("Warning", "Queue is empty!")

        def update_queue_display():
            queue_display.delete(0, tk.END)
            for item in self.queue:
                queue_display.insert(tk.END, item)

        tk.Button(queue_window, text="Enqueue", font=("Arial", 14), command=enqueue).pack(pady=5)
        tk.Button(queue_window, text="Dequeue", font=("Arial", 14), command=dequeue).pack(pady=5)

        queue_display = tk.Listbox(queue_window, font=("Arial", 14), height=10, width=30)
        queue_display.pack(pady=10)

    # Priority Queue Implementation
    def open_priority_queue_window(self):
        priority_queue_window = tk.Toplevel(self.master)
        priority_queue_window.title("Priority Queue Implementation")
        priority_queue_window.geometry("500x400")

        self.priority_queue = []

        def insert():
            value = simpledialog.askinteger("Input", "Enter a value to insert:")
            if value is not None:
                heapq.heappush(self.priority_queue, value)
                update_display()

        def remove():
            if self.priority_queue:
                heapq.heappop(self.priority_queue)
                update_display()
            else:
                messagebox.showwarning("Warning", "Priority Queue is empty!")

        def update_display():
            priority_queue_display.delete(0, tk.END)
            for item in self.priority_queue:
                priority_queue_display.insert(tk.END, item)

        tk.Button(priority_queue_window, text="Insert", font=("Arial", 14), command=insert).pack(pady=5)
        tk.Button(priority_queue_window, text="Remove", font=("Arial", 14), command=remove).pack(pady=5)

        priority_queue_display = tk.Listbox(priority_queue_window, font=("Arial", 14), height=10, width=30)
        priority_queue_display.pack(pady=10)

    # Binary Tree Implementation
    def open_binary_tree_window(self):
        binary_tree_window = tk.Toplevel(self.master)
        binary_tree_window.title("Binary Tree Implementation")
        binary_tree_window.geometry("500x400")

        class Node:
            def __init__(self, value):
                self.left = None
                self.right = None
                self.value = value

        self.b_tree_root = None

        def insert():
            value = simpledialog.askinteger("Input", "Enter a value to insert:")
            if value is not None:
                if self.b_tree_root is None:
                    self.b_tree_root = Node(value)
                else:
                    self.insert_into_bst(self.b_tree_root, value)
                update_display()

        def insert_into_bst(node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                else:
                    insert_into_bst(node.left, value)
            else:
                if node.right is None:
                    node.right = Node(value)
                else:
                    insert_into_bst(node.right, value)

        def update_display():
            binary_tree_display.delete(0, tk.END)
            self.in_order_traversal(self.b_tree_root, binary_tree_display)

        def in_order_traversal(node, display):
            if node:
                self.in_order_traversal(node.left, display)
                display.insert(tk.END, node.value)
                self.in_order_traversal(node.right, display)

        tk.Button(binary_tree_window, text="Insert", font=("Arial", 14), command=insert).pack(pady=5)

        binary_tree_display = tk.Listbox(binary_tree_window, font=("Arial", 14), height=10, width=30)
        binary_tree_display.pack(pady=10)

    # Huffman Coding Implementation (placeholder)
    def open_huffman_coding_window(self):
        huffman_window = tk.Toplevel(self.master)
        huffman_window.title("Huffman Coding Implementation")
        huffman_window.geometry("500x400")

        def huffman_coding():
            text = simpledialog.askstring("Input", "Enter text for Huffman Coding:")
            if text:
                frequency = collections.Counter(text)
                heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
                heapq.heapify(heap)

                while len(heap) > 1:
                    lo = heapq.heappop(heap)
                    hi = heapq.heappop(heap)
                    for pair in lo[1:]:
                        pair[1] = '0' + pair[1]
                    for pair in hi[1:]:
                        pair[1] = '1' + pair[1]
                    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

                huffman_tree = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
                huffman_result = {symbol: code for symbol, code in huffman_tree}
                messagebox.showinfo("Huffman Codes", f"Huffman Codes:\n{huffman_result}")

        tk.Button(huffman_window, text="Run Huffman Coding", font=("Arial", 14), command=huffman_coding).pack(pady=20)

    # BFS Graph Implementation
    def open_bfs_graph_window(self):
        bfs_graph_window = tk.Toplevel(self.master)
        bfs_graph_window.title("BFS Graph Implementation")
        bfs_graph_window.geometry("500x400")

        self.bfs_graph = nx.Graph()

        def add_edge():
            edge = simpledialog.askstring("Input", "Enter an edge (format: node1,node2):")
            if edge:
                nodes = edge.split(",")
                if len(nodes) == 2:
                    self.bfs_graph.add_edge(nodes[0], nodes[1])
                    update_graph_display()
                else:
                    messagebox.showwarning("Warning", "Invalid edge format!")

        def bfs_traversal():
            if self.bfs_graph.number_of_nodes() > 0:
                start_node = simpledialog.askstring("Input", "Enter the start node:")
                if start_node in self.bfs_graph.nodes:
                    visited = self.bfs_bfs(start_node)
                    self.show_graph("BFS Traversal", visited)
                else:
                    messagebox.showwarning("Warning", "Start node not in graph!")
            else:
                messagebox.showwarning("Warning", "Graph is empty!")

        def update_graph_display():
            graph_display.delete(0, tk.END)
            for edge in self.bfs_graph.edges:
                graph_display.insert(tk.END, edge)

        tk.Button(bfs_graph_window, text="Add Edge", font=("Arial", 14), command=add_edge).pack(pady=5)
        tk.Button(bfs_graph_window, text="BFS Traversal", font=("Arial", 14), command=bfs_traversal).pack(pady=5)

        graph_display = tk.Listbox(bfs_graph_window, font=("Arial", 14), height=10, width=40)
        graph_display.pack(pady=10)

    def bfs_bfs(self, start):
        visited = []
        queue = collections.deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                neighbors = list(self.bfs_graph.neighbors(node))
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited

    def show_graph(self, title, visited):
        plt.figure()
        pos = nx.spring_layout(self.bfs_graph)
        nx.draw(self.bfs_graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_color='black')
        nx.draw_networkx_nodes(self.bfs_graph, pos, nodelist=visited, node_color='orange')
        plt.title(title)
        plt.show()

    # DFS Graph Implementation
    def open_dfs_graph_window(self):
        dfs_graph_window = tk.Toplevel(self.master)
        dfs_graph_window.title("DFS Graph Implementation")
        dfs_graph_window.geometry("500x400")

        self.dfs_graph = nx.Graph()

        def add_edge():
            edge = simpledialog.askstring("Input", "Enter an edge (format: node1,node2):")
            if edge:
                nodes = edge.split(",")
                if len(nodes) == 2:
                    self.dfs_graph.add_edge(nodes[0], nodes[1])
                    update_graph_display()
                else:
                    messagebox.showwarning("Warning", "Invalid edge format!")

        def dfs_traversal():
            if self.dfs_graph.number_of_nodes() > 0:
                start_node = simpledialog.askstring("Input", "Enter the start node:")
                if start_node in self.dfs_graph.nodes:
                    visited = self.dfs_dfs(start_node)
                    self.show_graph("DFS Traversal", visited)
                else:
                    messagebox.showwarning("Warning", "Start node not in graph!")
            else:
                messagebox.showwarning("Warning", "Graph is empty!")

        def update_graph_display():
            graph_display.delete(0, tk.END)
            for edge in self.dfs_graph.edges:
                graph_display.insert(tk.END, edge)

        tk.Button(dfs_graph_window, text="Add Edge", font=("Arial", 14), command=add_edge).pack(pady=5)
        tk.Button(dfs_graph_window, text="DFS Traversal", font=("Arial", 14), command=dfs_traversal).pack(pady=5)

        graph_display = tk.Listbox(dfs_graph_window, font=("Arial", 14), height=10, width=40)
        graph_display.pack(pady=10)

    def dfs_dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                neighbors = list(self.dfs_graph.neighbors(node))
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return visited

    # Hash Table with Collision Handling Implementation (placeholder)
    def open_collision_hash_table_window(self):
        collision_hash_table_window = tk.Toplevel(self.master)
        collision_hash_table_window.title("Hash Table with Collision Handling")
        collision_hash_table_window.geometry("500x400")

        self.hash_table = {}

        def insert():
            key = simpledialog.askstring("Input", "Enter key:")
            value = simpledialog.askstring("Input", "Enter value:")
            if key and value:
                if key in self.hash_table:
                    self.hash_table[key].append(value)
                else:
                    self.hash_table[key] = [value]
                update_display()

        def update_display():
            collision_display.delete(0, tk.END)
            for key, values in self.hash_table.items():
                collision_display.insert(tk.END, f"{key}: {', '.join(values)}")

        tk.Button(collision_hash_table_window, text="Insert", font=("Arial", 14), command=insert).pack(pady=5)

        collision_display = tk.Listbox(collision_hash_table_window, font=("Arial", 14), height=10, width=50)
        collision_display.pack(pady=10)

    # Abstract Data Type Implementation (placeholder)
    def open_adt_window(self):
            adt_window = tk.Toplevel(self.master)
            adt_window.title("Abstract Data Type Implementation")
            adt_window.geometry("500x400")

            self.adt_list = []

            def add_element():
                value = simpledialog.askstring("Input", "Enter a value to add:")
                if value:
                    self.adt_list.append(value)
                    update_display()

            def remove_element():
                if self.adt_list:
                    value = simpledialog.askstring("Input", "Enter a value to remove:")
                    if value in self.adt_list:
                        self.adt_list.remove(value)
                        update_display()
                    else:
                        messagebox.showwarning("Warning", "Value not found!")

            def update_display():
                adt_display.delete(0, tk.END)
                for item in self.adt_list:
                    adt_display.insert(tk.END, item)

            tk.Button(adt_window, text="Add Element", font=("Arial", 14), command=add_element).pack(pady=5)
            tk.Button(adt_window, text="Remove Element", font=("Arial", 14), command=remove_element).pack(pady=5)

            adt_display = tk.Listbox(adt_window, font=("Arial", 14), height=10, width=30)
            adt_display.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app =DataStructuresGUI(root)
    root.mainloop()
