import shutil
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi
from os import mkdir, path
from PIL import Image

first_source_frequency = int(input("First source frequency (integer): "))
second_source_frequency = int(input("Second source frequency (integer): "))
curve_colour = input("Colour of the Lissajous curve (r/g/b/c/m/y): ")
number_of_iterations = int(input("Number of iterations (frames in .gif) (integer): "))
phase_step = int(input("Phase step (integer): "))
result_directory_name = "Lissajous curves"


def create_result_directory():
    if path.exists(result_directory_name):
        shutil.rmtree(result_directory_name)
        mkdir(result_directory_name)
    else:
        mkdir(result_directory_name)


def draw_lissajous_curves():

    create_result_directory()

    for iteration in range(number_of_iterations):
        phi = iteration / phase_step
        phase_shift = phi * pi

        x = [sin(first_source_frequency * i + phase_shift) for i in np.arange(0., 2 * pi, 0.0001)]
        y = [sin(second_source_frequency * j) for j in np.arange(0., 2 * pi, 0.0001)]

        plt.plot(y, x, curve_colour)
        plt.title(f"Phase shift: {phi}π.")

        plt.grid(True)

        plt.savefig(path.join(result_directory_name, f"Lissajous curve {iteration}.png"))
        plt.close()


def convert_frames_to_gif():
    frames = []

    for frame_number in range(number_of_iterations):
        frame = Image.open(path.join(result_directory_name, f"Lissajous curve {frame_number}.png"))
        frames.append(frame)

    frames[0].save(
        path.join(result_directory_name, "Lissajous curves.gif"),
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=100,
        loop=0
    )


draw_lissajous_curves()
convert_frames_to_gif()
