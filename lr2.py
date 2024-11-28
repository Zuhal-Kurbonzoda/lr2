import tkinter as tk
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def brezenhem_algorithm(new_x, new_y, radius):
    image = Image.new('RGB', (1000, 500), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    decision = 3 - 2 * radius
    current_x, current_y = 0, radius
    while current_x <= current_y:
        draw.point((new_x + current_x, new_y + current_y), fill=(255, 0, 0))
        draw.point((new_x + current_y, new_y + current_x), fill=(255, 0, 0))
        draw.point((new_x - current_x, new_y + current_y), fill=(255, 0, 0))
        draw.point((new_x - current_y, new_y + current_x), fill=(255, 0, 0))
        draw.point((new_x + current_x, new_y - current_y), fill=(255, 0, 0))
        draw.point((new_x + current_y, new_y - current_x), fill=(255, 0, 0))
        draw.point((new_x - current_x, new_y - current_y), fill=(255, 0, 0))
        draw.point((new_x - current_y, new_y - current_x), fill=(255, 0, 0))
        if decision < 0:
            decision += 4 * current_x + 6
        else:
            decision += 4 * (current_x - current_y) + 10
            current_y -= 1
        current_x += 1
    return np.array(image)


def circle_formula(new_x, new_y, radius):
    image = Image.new('RGB', (1000, 500), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for i in range(-radius*10, radius*10+1):
        for j in range(-radius*10, radius*10+1):
            if abs(i**2/100 + j**2/100 - radius**2) <= 1:
                draw.point((new_x + i//10, new_y + j//10), fill=(255, 0, 0))
    return np.array(image)



def trigonometric_formula(new_x, new_y, radius):
    image = Image.new('RGB', (1000, 500), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    for i in range(720):
        angle = i * np.pi / 180
        current_x = new_x + radius * np.cos(angle)
        current_y = new_y + radius * np.sin(angle)
        draw.point((int(current_x), int(current_y)), fill=(255, 0, 0))
    return np.array(image)


class AlgorithmPlot:
    def __init__(self, root):
        self.root = root
        self.root.title("Алгоритмы")
        self.create_widgets()

    def create_widgets(self):
        self.label_x = tk.Label(self.root, text="x:")
        self.label_x.grid(row=0, column=0)
        self.entry_x = tk.Entry(self.root)
        self.entry_x.grid(row=0, column=1)

        self.label_y = tk.Label(self.root, text="y:")
        self.label_y.grid(row=0, column=2)
        self.entry_y = tk.Entry(self.root)
        self.entry_y.grid(row=0, column=3)

        self.label_radius = tk.Label(self.root, text="r:")
        self.label_radius.grid(row=1, column=0)
        self.entry_radius = tk.Entry(self.root)
        self.entry_radius.grid(row=1, column=1)

        self.button_plot = tk.Button(self.root, text="Построить", command=self.plot)
        self.button_plot.grid(row=2, column=0, columnspan=4)

        self.figure, self.axis = plt.subplots()
        self.axis.set_title("Алгоритмы")
        self.axis.set_axis_off()
        self.buttons = [
            plt.Button(plt.axes([0.1, 0.05, 0.2, 0.075]), 'Триг. Формула'),
            plt.Button(plt.axes([0.4, 0.05, 0.2, 0.075]), 'Брезенхема'),
            plt.Button(plt.axes([0.7, 0.05, 0.2, 0.075]), 'Формула круга')
        ]
        self.buttons[0].on_clicked(self.plot_trigonometric_formula)
        self.buttons[1].on_clicked(self.plot_brezenhem_algorithm)
        self.buttons[2].on_clicked(self.plot_circle_formula)

    def plot(self):
        self.new_x = int(self.entry_x.get())
        self.new_y = int(self.entry_y.get())
        self.radius = int(self.entry_radius.get())
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(trigonometric_formula(self.new_x, self.new_y, self.radius))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм тригонометрической формулы")

    def plot_trigonometric_formula(self, event):
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(trigonometric_formula(self.new_x, self.new_y, self.radius))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм тригонометрической формулы")
                            
    def plot_brezenhem_algorithm(self, event):
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(brezenhem_algorithm(self.new_x, self.new_y, self.radius))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм Брезенхема")

    def plot_circle_formula(self, event):
        self.axis.clear()
        plt.show(block=False)
        self.axis.imshow(circle_formula(self.new_x, self.new_y, self.radius))
        plt.subplots_adjust(top=1.0, bottom=0.2, left=0.1, right=0.9)
        self.axis.set_title("Алгоритм формулы круга")


def main():
    root = tk.Tk()
    AlgorithmPlot(root)
    root.mainloop()


if __name__ == "__main__":
    main()