import tkinter as tk
from particle_sim import get_graph
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Magnetic Modeling")

# Add image file 
bg = ImageTk.PhotoImage(Image.open("/Users/anshmenghani/Downloads/jwstDeepField.png"))
  
# Show image using label 
label1 = tk.Label(root, image=bg) 
label1.place(x = -300, y = 0) 

label = tk.Label(root, text="Magnetic Modeling", font=("Lexend", 24, "bold"))
label.pack(pady=10)

blank_line = tk.Label(root, text="")
blank_line.pack()

# Add a label
top_label = tk.Label(root, text="Specify Initial Paramaters of the Particle", font=("Lexend", 18, "italic"))
top_label.pack()

blank_line = tk.Label(root, text="")
blank_line.pack()

posx_label = tk.Label(root, text="Initial X-Coordinate: ")
posx_label.pack()
posx = tk.Entry(root)
posx.insert(0, "in earth radii") 
posx.pack(pady=10)

posy_label = tk.Label(root, text="Initial Y-Coordinate: ")
posy_label.pack()
posy = tk.Entry(root)
posy.insert(0, "in earth radii") 
posy.pack(pady=10)

posz_label = tk.Label(root, text="Initial Z-Coordinate: ")
posz_label.pack()
posz = tk.Entry(root)
posz.insert(0, "in earth radii") 
posz.pack(pady=10)

velx_label = tk.Label(root, text="Initial X-Velocity: ")
velx_label.pack()
velx = tk.Entry(root)
velx.insert(0, "in earth radii per second") 
velx.pack(pady=10)

vely_label = tk.Label(root, text="Initial Y-Velocity: ")
vely_label.pack()
vely = tk.Entry(root)
vely.insert(0, "in earth radii per second") 
vely.pack(pady=10)

velz_label = tk.Label(root, text="Initial Z-Velocity: ")
velz_label.pack()
velz = tk.Entry(root)
velz.insert(0, "in earth radii per second") 
velz.pack(pady=10)

def get_text():
    coords = [float(posx.get()), float(posy.get()), float(posz.get())]
    vels = [float(velx.get()), float(vely.get()), float(velz.get())]
    get_graph(coords, vels)

# Add a button to get the text
get_text_button = tk.Button(root, text="Get Path Graph", command=get_text)
get_text_button.pack(pady=10)

# Run the main loop
root.mainloop()
