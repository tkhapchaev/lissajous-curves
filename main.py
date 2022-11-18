import shutil
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi
from os import mkdir, path


def create_result_directory(result_directory_path):
    if path.exists(result_directory_path):
        shutil.rmtree(result_directory_path)
        mkdir(result_directory_path)
    else:
        mkdir(result_directory_path)


def draw_lissajous_curves(first_source_frequency, second_source_frequency, number_of_iterations, phase_step,
                          curve_colour, result_directory_name):

    create_result_directory(result_directory_name)

    for iteration in range(number_of_iterations):
        phi = iteration / phase_step
        phase_shift = phi * pi

        x = [sin(first_source_frequency * i + phase_shift) for i in np.arange(0., 2 * pi, 0.0001)]
        y = [sin(second_source_frequency * j) for j in np.arange(0., 2 * pi, 0.0001)]

        plt.plot(y, x, curve_colour)
        plt.title("Phase shift: " + str(phi) + "π.")

        plt.grid(True)

        plt.savefig(path.join(result_directory_name, "Lissajous curve " + str(iteration) + ".png"))
        plt.close()


draw_lissajous_curves(3, 4, 100, 100, "r", "Lissajous curves")
