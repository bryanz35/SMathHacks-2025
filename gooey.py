import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Magnetic Modeling")

label = tk.Label(root, text="Magnetic Modeling")
label.pack(pady=10)

# Add a label
top_label = tk.Label(root, text="Specify Initial Paramaters of Particle")
top_label.pack()

posx_label = tk.Label(root, text="Initial X-Coordinate: ")
posx_label.pack()
posx = tk.Entry(root)
posx.pack(pady=10)

posy_label = tk.Label(root, text="Initial Y-Coordinate: ")
posy_label.pack()
posy = tk.Entry(root)
posy.pack(pady=10)

posz_label = tk.Label(root, text="Initial Z-Coordinate: ")
posz_label.pack()
posz = tk.Entry(root)
posz.pack(pady=10)

button = tk.Button(root, text="Click Me", command=lambda: print("Button Clicked!"))
button.pack(pady=10)

# Add an entry field


# Function to get the text from the entry field
def get_text():
    text = posx.get()
    print("Entered text:", text)

# Add a button to get the text
get_text_button = tk.Button(root, text="Get Text", command=get_text)
get_text_button.pack(pady=10)

# Run the main loop
root.mainloop()
