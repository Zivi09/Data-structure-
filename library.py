import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import bcrypt
import os
import sqlite3

# Database Setup
def setup_database():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE,
                    password TEXT,
                    is_admin INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    image_path TEXT)''')
    conn.commit()
    conn.close()

setup_database()

# Hash Password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Check Password
def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

# User Authentication
def authenticate_user(username, password):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT password, is_admin FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    
    if result and check_password(result[0], password):
        return result[1]  # return is_admin status
    return None

# User Registration
def register_user(username, password, is_admin=False):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)',
              (username, hash_password(password), int(is_admin)))
    conn.commit()
    conn.close()

# Add Book
def add_book(title, author, image_path):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('INSERT INTO books (title, author, image_path) VALUES (?, ?, ?)',
              (title, author, image_path))
    conn.commit()
    conn.close()

# Fetch Books
def fetch_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute('SELECT * FROM books')
    books = c.fetchall()
    conn.close()
    return books

# GUI Application
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")
        self.create_sidebar()
        self.create_home_frame()  # Show home frame by default
        
    def create_sidebar(self):
        self.sidebar = ttk.Frame(self.root, width=200)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(self.sidebar, text="Library Management", font=self.title_font).pack(pady=10)

        ttk.Button(self.sidebar, text="Home", command=self.create_home_frame).pack(pady=5, padx=10, fill=tk.X)
        ttk.Button(self.sidebar, text="Books", command=self.create_books_frame).pack(pady=5, padx=10, fill=tk.X)

        # Example of Button Hover Effect
        login_button = ttk.Button(self.sidebar, text="Login / Signup", command=self.create_login_frame)
        login_button.pack(pady=5, padx=10, fill=tk.X)

        # Hover Effect
        login_button.bind("<Enter>", lambda e: e.widget.config(style='TButtonHover'))
        login_button.bind("<Leave>", lambda e: e.widget.config(style='TButton'))

        ttk.Button(self.sidebar, text="Admin Login", command=self.create_admin_login_frame).pack(pady=5, padx=10, fill=tk.X)

    def create_home_frame(self):
        self.clear_main_area()
        ttk.Label(self.root, text="Welcome to the Library Management System", font=self.title_font).pack(pady=20)
    def create_home_frame(self):
        self.clear_main_area()
        ttk.Label(self.root, text="Welcome to the Library Management System", font=self.title_font).pack(pady=20)

    def create_books_frame(self):
        self.clear_main_area()
        tk.Label(self.root, text="Books List", font=("Arial", 18)).pack(pady=10)

        books = fetch_books()
        for i, (book_id, title, author, image_path) in enumerate(books):
            tk.Label(self.root, text=f"{title} by {author}", font=("Arial", 14)).pack(pady=5)
            if image_path:
                img = tk.PhotoImage(file=image_path)
                img_label = tk.Label(self.root, image=img)
                img_label.image = img  # keep a reference!
                img_label.pack(pady=5)

        tk.Button(self.root, text="Back to Home", command=self.create_home_frame).pack(pady=20)

    def create_members_frame(self):
        self.clear_main_area()
        tk.Label(self.root, text="Members Management", font=("Arial", 18)).pack(pady=10)
        tk.Button(self.root, text="Back to Home", command=self.create_home_frame).pack(pady=20)

    def create_add_book_frame(self):
        self.clear_main_area()
        
        tk.Label(self.root, text="Add New Book", font=("Arial", 18)).pack(pady=10)
        
        tk.Label(self.root, text="Title").pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        tk.Label(self.root, text="Author").pack()
        self.author_entry = tk.Entry(self.root)
        self.author_entry.pack()

        tk.Button(self.root, text="Upload Image", command=self.upload_image).pack(pady=5)
        self.image_path_label = tk.Label(self.root, text="No file selected")
        self.image_path_label.pack()

        tk.Button(self.root, text="Add Book", command=self.add_book).pack(pady=5)
        tk.Button(self.root, text="Back to Home", command=self.create_home_frame).pack(pady=20)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if self.image_path:
            self.image_path_label.config(text=os.path.basename(self.image_path))

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        
        if title and author and hasattr(self, 'image_path'):
            add_book(title, author, self.image_path)
            messagebox.showinfo("Success", "Book added successfully!")
            self.create_home_frame()
        else:
            messagebox.showerror("Error", "Please fill all fields and upload an image.")

    def create_login_frame(self):
        self.clear_main_area()
        
        tk.Label(self.root, text="Login", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.create_register_frame).pack(pady=5)
        tk.Button(self.root, text="Back to Home", command=self.create_home_frame).pack(pady=20)

    def create_register_frame(self):
        self.clear_main_area()
        
        tk.Label(self.root, text="Register", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        tk.Label(self.root, text="Admin (Check if Admin)").pack()
        self.is_admin_var = tk.BooleanVar()
        tk.Checkbutton(self.root, variable=self.is_admin_var).pack()

        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)
        tk.Button(self.root, text="Back to Login", command=self.create_login_frame).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        is_admin = authenticate_user(username, password)
        
        if is_admin is True:
            self.create_admin_panel()
        elif is_admin is False:
            self.create_user_profile()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        is_admin = self.is_admin_var.get()
        
        try:
            register_user(username, password, is_admin)
            messagebox.showinfo("Success", "User registered successfully!")
            self.create_login_frame()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def create_admin_panel(self):
        self.clear_main_area()
        tk.Label(self.root, text="Admin Panel", font=("Arial", 24)).pack(pady=20)

    def create_user_profile(self):
        self.clear_main_area()
        tk.Label(self.root, text="User Profile", font=("Arial", 24)).pack(pady=20)

    def create_admin_login_frame(self):
        self.clear_main_area()
        
        tk.Label(self.root, text="Admin Login", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        self.admin_username_entry = tk.Entry(self.root)
        self.admin_username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.admin_password_entry = tk.Entry(self.root, show='*')
        self.admin_password_entry.pack()

        tk.Button(self.root, text="Login", command=self.admin_login).pack(pady=5)
        tk.Button(self.root, text="Back to Home", command=self.create_home_frame).pack(pady=20)

    def admin_login(self):
        # Implement admin login logic
        username = self.admin_username_entry.get()
        password = self.admin_password_entry.get()
        if username == "admin" and password == "admin123":
            self.create_admin_panel()
        else:
            messagebox.showerror("Error", "Invalid admin credentials")

    def clear_main_area(self):
        for widget in self.root.winfo_children():
            if widget.winfo_y() > 0:  # clear only main area, keep sidebar
                widget.destroy()

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
