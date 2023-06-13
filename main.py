import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def evaluate_expression(expr, x):
    return eval(expr)

def plot():
    ax.clear()
    func = entry.get()
    x = np.linspace(-10, 10, 400)
    y = evaluate_expression(func, x)
    ax.plot(x, y)
    ax.grid(True)
    ax.axhline(0, color='black',linewidth=0.5)
    ax.axvline(0, color='black',linewidth=0.5)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    canvas.draw()

root = tk.Tk()
root.geometry("800x600")

figure = plt.Figure(figsize=(5, 4), dpi=100)
ax = figure.add_subplot(111)
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack()

entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Enter Function", command=plot)
button.pack()

root.mainloop()
