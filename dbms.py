import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
import collections
import heapq
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image, ImageTk

class DBMSAPP:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Structure Simulator: Interactive Learning Tool Introduction:")
        self.master.geometry("1200x800")
        self.master.config(bg="#F5F5F5")  # Light background color for the main window

        # Set up styles for buttons and labels
        self.setup_styles()

        # Load and set background image (adjust path as necessary)
        bg_image_path = "C:/Users/Ziven/Downloads/WhatsApp Image 2024-06-18 at 9.39.52 PM.jpeg"  
        self.bg_image = Image.open(bg_image_path)
        self.bg_image = self.bg_image.resize((1500, 1000), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        bg_label = tk.Label(self.master, image=self.bg_image_tk)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title Label
        title_label = tk.Label(self.master, text="Data Structure Simulator: Interactive Learning Tool Introduction:", font=("Helvetica", 32, "bold"), bg="#4682B4", fg="white", padx=20, pady=10)
        title_label.pack(side=tk.TOP, fill=tk.X)

        # Create a sidebar for navigation
        self.sidebar_frame = tk.Frame(self.master, bg="#2F4F4F", width=200, relief=tk.RIDGE)
        self.sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Create buttons with icons (use placeholder text/icons for now)
        buttons = [
            ("Stack (Query History)", self.open_stack_window, "📚"),
            ("Singly Linked List (Records)", self.open_singly_linked_list_window, "📄"),
            ("Doubly Linked List (Data Records)", self.open_doubly_linked_list_window, "🔗"),
            ("Queue (Query Queue)", self.open_queue_window, "📝"),
            ("Priority Queue (Query Optimizer)", self.open_priority_queue_window, "⚡"),
            ("Binary Tree (Efficient Search)", self.open_binary_tree_window, "🌳"),
            ("Huffman Coding (Compression)", self.open_huffman_coding_window, "🔒"),
            ("BFS Graph (Data Analysis)", self.open_bfs_graph_window, "🔍"),
            ("DFS Graph (Search Records)", self.open_dfs_graph_window, "🔎"),
            ("Hash Table (Efficient Lookup)", self.open_hash_table_window, "🔑")
        ]

        for idx, (text, command, icon) in enumerate(buttons):
            btn = tk.Button(self.sidebar_frame, text=f"{icon} {text}", font=("Helvetica", 12), command=command, relief="flat", bg="#2F4F4F", fg="white", activebackground="#4682B4", activeforeground="white")
            btn.pack(fill=tk.X, pady=5, padx=10, ipady=10)

        # Main visualization area
        self.visual_frame = tk.Frame(self.master, bg="white", relief=tk.SUNKEN, borderwidth=3)
        self.visual_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Example visualization placeholder label
        self.visual_label = tk.Label(self.visual_frame, text="Visualizations will appear here", font=("Helvetica", 16), bg="white")
        self.visual_label.pack(expand=True)

        # Dark/Light mode toggle button
    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
            self.root.config(bg="black")
            self.sidebar_frame.config(bg="black")
            self.theme_button.config(bg="black", fg="white")
            self.open_db_button.config(bg="black", fg="white")
            self.main_frame.config(bg="black")
        else:
            self.current_theme = "light"
            self.root.config(bg="white")
            self.sidebar_frame.config(bg="#2F4F4F")
            self.theme_button.config(bg="#2F4F4F", fg="white")
            self.open_db_button.config(bg="#2F4F4F", fg="white")
            self.main_frame.config(bg="white")
              


    def setup_styles(self):
        """Sets up visual styles for buttons and other widgets."""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=("Helvetica", 12), padding=10)

    def open_stack_window(self):
        self.stack_window = tk.Toplevel(self.master)
        self.stack_window.title("Query History (Stack)")
        self.stack_window.geometry("500x400")

        self.stack = []

        def push_query():
            query = simpledialog.askstring("New Query", "Enter the query:")
            if query:
                self.stack.append(query)
                update_stack_display()

        def pop_query():
            if self.stack:
                popped_query = self.stack.pop()
                messagebox.showinfo("Query Executed", f"Query executed: {popped_query}")
                update_stack_display()
            else:
                messagebox.showwarning("Warning", "Query history is empty!")

        def update_stack_display():
            stack_display.delete(0, tk.END)
            for query in reversed(self.stack):
                stack_display.insert(tk.END, query)

        tk.Button(self.stack_window, text="Add Query", command=push_query).pack(pady=5)
        tk.Button(self.stack_window, text="Execute Last Query", command=pop_query).pack(pady=5)

        stack_display = tk.Listbox(self.stack_window, font=("Arial", 14), height=10, width=40)
        stack_display.pack(pady=10)

    def open_singly_linked_list_window(self):
        self.sll_window = tk.Toplevel(self.master)
        self.sll_window.title("Records (Singly Linked List)")
        self.sll_window.geometry("500x400")

        class Node:
            def __init__(self, data):
                self.data = data
                self.next = None

        self.sll_head = None

        def insert_record():
            value = simpledialog.askstring("Insert Record", "Enter the record:")
            if value:
                new_node = Node(value)
                new_node.next = self.sll_head
                self.sll_head = new_node
                update_display()

        def delete_record():
            if self.sll_head:
                self.sll_head = self.sll_head.next
                update_display()
            else:
                messagebox.showwarning("Warning", "No records to delete!")

        def update_display():
            sll_display.delete(0, tk.END)
            current = self.sll_head
            while current:
                sll_display.insert(tk.END, current.data)
                current = current.next

        tk.Button(self.sll_window, text="Insert Record", command=insert_record).pack(pady=5)
        tk.Button(self.sll_window, text="Delete First Record", command=delete_record).pack(pady=5)

        sll_display = tk.Listbox(self.sll_window, font=("Arial", 14), height=10, width=40)
        sll_display.pack(pady=10)

    def open_doubly_linked_list_window(self):
        self.dll_window = tk.Toplevel(self.master)
        self.dll_window.title("Data Records (Doubly Linked List)")
        self.dll_window.geometry("500x400")

        class Node:
            def __init__(self, data):
                self.data = data
                self.prev = None
                self.next = None

        self.dll_head = None

        def insert_data():
            value = simpledialog.askstring("Insert Data", "Enter the data:")
            if value:
                new_node = Node(value)
                new_node.next = self.dll_head
                if self.dll_head:
                    self.dll_head.prev = new_node
                self.dll_head = new_node
                update_display()

        def delete_data():
            if self.dll_head:
                self.dll_head = self.dll_head.next
                if self.dll_head:
                    self.dll_head.prev = None
                update_display()
            else:
                messagebox.showwarning("Warning", "No data to delete!")

        def update_display():
            dll_display.delete(0, tk.END)
            current = self.dll_head
            while current:
                dll_display.insert(tk.END, current.data)
                current = current.next

        tk.Button(self.dll_window, text="Insert Data", command=insert_data).pack(pady=5)
        tk.Button(self.dll_window, text="Delete First Data", command=delete_data).pack(pady=5)

        dll_display = tk.Listbox(self.dll_window, font=("Arial", 14), height=10, width=40)
        dll_display.pack(pady=10)

    def open_queue_window(self):
        self.queue_window = tk.Toplevel(self.master)
        self.queue_window.title("Query Queue (Queue)")
        self.queue_window.geometry("500x400")

        self.queue = collections.deque()

        def enqueue_query():
            query = simpledialog.askstring("New Query", "Enter the query:")
            if query:
                self.queue.append(query)
                update_queue_display()

        def dequeue_query():
            if self.queue:
                dequeued_query = self.queue.popleft()
                messagebox.showinfo("Query Executed", f"Query executed: {dequeued_query}")
                update_queue_display()
            else:
                messagebox.showwarning("Warning", "Queue is empty!")

        def update_queue_display():
            queue_display.delete(0, tk.END)
            for query in self.queue:
                queue_display.insert(tk.END, query)

        tk.Button(self.queue_window, text="Add Query", command=enqueue_query).pack(pady=5)
        tk.Button(self.queue_window, text="Execute Next Query", command=dequeue_query).pack(pady=5)

        queue_display = tk.Listbox(self.queue_window, font=("Arial", 14), height=10, width=40)
        queue_display.pack(pady=10)

    def open_priority_queue_window(self):
        self.pq_window = tk.Toplevel(self.master)
        self.pq_window.title("Query Optimizer (Priority Queue)")
        self.pq_window.geometry("500x400")

        self.priority_queue = []

        def insert_query():
            query = simpledialog.askstring("Insert Query", "Enter the query:")
            priority = simpledialog.askinteger("Priority", "Enter the priority (lower numbers indicate higher priority):")
            if query and priority is not None:
                heapq.heappush(self.priority_queue, (priority, query))
                update_pq_display()

        def execute_query():
            if self.priority_queue:
                priority, query = heapq.heappop(self.priority_queue)
                messagebox.showinfo("Query Executed", f"Query executed: {query}")
                update_pq_display()
            else:
                messagebox.showwarning("Warning", "Priority queue is empty!")

        def update_pq_display():
            pq_display.delete(0, tk.END)
            for priority, query in sorted(self.priority_queue):
                pq_display.insert(tk.END, f"{query} (Priority: {priority})")

        tk.Button(self.pq_window, text="Insert Query", command=insert_query).pack(pady=5)
        tk.Button(self.pq_window, text="Execute Highest Priority Query", command=execute_query).pack(pady=5)

        pq_display = tk.Listbox(self.pq_window, font=("Arial", 14), height=10, width=40)
        pq_display.pack(pady=10)

    def open_binary_tree_window(self):
        self.bt_window = tk.Toplevel(self.master)
        self.bt_window.title("Efficient Search (Binary Tree)")
        self.bt_window.geometry("500x400")

        class Node:
            def __init__(self, key):
                self.left = None
                self.right = None
                self.val = key

        self.bt_root = None

        def insert_node():
            key = simpledialog.askinteger("Insert Node", "Enter the node value:")
            if key is not None:
                self.bt_root = self._insert(self.bt_root, key)
                messagebox.showinfo("Node Inserted", f"Node {key} inserted.")
        
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.val:
                node.left = self._insert(node.left, key)
            else:
                node.right = self._insert(node.right, key)
            return node

        def visualize_tree():
            if not self.bt_root:
                messagebox.showwarning("Warning", "Tree is empty!")
                return
            
            g = nx.Graph()
            self._add_edges(g, self.bt_root)
            pos = nx.spring_layout(g)
            plt.figure()
            nx.draw(g, pos, with_labels=True, arrows=True)
            plt.title("Binary Tree Visualization")
            plt.show()

        def _add_edges(g, node):
            if node is not None:
                if node.left:
                    g.add_edge(node.val, node.left.val)
                    _add_edges(g, node.left)
                if node.right:
                    g.add_edge(node.val, node.right.val)
                    _add_edges(g, node.right)

        tk.Button(self.bt_window, text="Insert Node", command=insert_node).pack(pady=5)
        tk.Button(self.bt_window, text="Visualize Tree", command=visualize_tree).pack(pady=5)

    def open_huffman_coding_window(self):
        self.huffman_window = tk.Toplevel(self.master)
        self.huffman_window.title("Compression (Huffman Coding)")
        self.huffman_window.geometry("500x400")

        def huffman_encoding():
            text = simpledialog.askstring("Input Text", "Enter the text to encode:")
            if text:
                frequency = collections.Counter(text)
                heap = [[weight, [char, ""]] for char, weight in frequency.items()]
                heapq.heapify(heap)

                while len(heap) > 1:
                    lo = heapq.heappop(heap)
                    hi = heapq.heappop(heap)
                    for pair in lo[1:]:
                        pair[1] = '0' + pair[1]
                    for pair in hi[1:]:
                        pair[1] = '1' + pair[1]
                    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
                huffman_code = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p[0]))

                huffman_display.delete(0, tk.END)
                for p in huffman_code:
                    huffman_display.insert(tk.END, f"{p[0]}: {p[1]}")

        tk.Button(self.huffman_window, text="Encode Text", command=huffman_encoding).pack(pady=5)

        huffman_display = tk.Listbox(self.huffman_window, font=("Arial", 14), height=10, width=40)
        huffman_display.pack(pady=10)

    def open_bfs_graph_window(self):
        self.bfs_window = tk.Toplevel(self.master)
        self.bfs_window.title("Data Analysis (BFS Graph)")
        self.bfs_window.geometry("500x400")

        self.graph_bfs = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

        def bfs_traversal():
            start_node = simpledialog.askstring("Start Node", "Enter the start node:")
            if start_node not in self.graph_bfs:
                messagebox.showwarning("Warning", "Start node not in graph!")
                return

            visited = []
            queue = collections.deque([start_node])
            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.append(node)
                    queue.extend(neighbor for neighbor in self.graph_bfs[node] if neighbor not in visited)

            bfs_display.delete(0, tk.END)
            bfs_display.insert(tk.END, " -> ".join(visited))

        tk.Button(self.bfs_window, text="Perform BFS", command=bfs_traversal).pack(pady=5)

        bfs_display = tk.Listbox(self.bfs_window, font=("Arial", 14), height=10, width=40)
        bfs_display.pack(pady=10)

    def open_dfs_graph_window(self):
        self.dfs_window = tk.Toplevel(self.master)
        self.dfs_window.title("Search Records (DFS Graph)")
        self.dfs_window.geometry("500x400")

        self.graph_dfs = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['F'],
            'F': []
        }

        def dfs_traversal():
            start_node = simpledialog.askstring("Start Node", "Enter the start node:")
            if start_node not in self.graph_dfs:
                messagebox.showwarning("Warning", "Start node not in graph!")
                return

            visited = set()

            def dfs(node):
                if node not in visited:
                    visited.add(node)
                    for neighbor in self.graph_dfs[node]:
                        dfs(neighbor)

            dfs(start_node)
            dfs_display.delete(0, tk.END)
            dfs_display.insert(tk.END, " -> ".join(visited))

        tk.Button(self.dfs_window, text="Perform DFS", command=dfs_traversal).pack(pady=5)

        dfs_display = tk.Listbox(self.dfs_window, font=("Arial", 14), height=10, width=40)
        dfs_display.pack(pady=10)

    def open_hash_table_window(self):
        self.hash_window = tk.Toplevel(self.master)
        self.hash_window.title("Efficient Lookup (Hash Table)")
        self.hash_window.geometry("500x400")

        self.hash_table = {}

        def insert_entry():
            key = simpledialog.askstring("Key", "Enter the key:")
            value = simpledialog.askstring("Value", "Enter the value:")
            if key and value:
                self.hash_table[key] = value
                update_display()

        def delete_entry():
            key = simpledialog.askstring("Key", "Enter the key to delete:")
            if key in self.hash_table:
                del self.hash_table[key]
                update_display()
            else:
                messagebox.showwarning("Warning", "Key not found!")

        def update_display():
            hash_display.delete(0, tk.END)
            for key, value in self.hash_table.items():
                hash_display.insert(tk.END, f"{key}: {value}")

        tk.Button(self.hash_window, text="Insert Entry", command=insert_entry).pack(pady=5)
        tk.Button(self.hash_window, text="Delete Entry", command=delete_entry).pack(pady=5)

        hash_display = tk.Listbox(self.hash_window, font=("Arial", 14), height=10, width=40)
        hash_display.pack(pady=10)
    
    def __init__(self, cities, distance_matrix):
        self.cities = cities
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def calculate_total_distance(self, route):
        total_distance = sum(self.distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        total_distance += self.distance_matrix[route[-1]][route[0]]
        return total_distance

    


    def run(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app =DBMSAPP(root)
    app.run()
