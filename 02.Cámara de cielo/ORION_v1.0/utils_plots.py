#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def plot_matrix(data, title, type):
    plt.title(title)
    plt.imshow(data)
    plt.colorbar()
    plt.savefig("data/tmp/" + type + ".png", dpi=600, bbox_inches="tight")
    plt.close()


def plot_pixel_distances(distances, max, size):
    mean = []
    for i in np.arange(0, size):
        mean.append(np.mean(distances))
    plt.xlabel("Image number", fontsize=12)
    plt.ylabel("Pixel distance (arcmin)", fontsize=12)
    plt.ylim(0, max + 1)
    plt.xlim(0, size)
    plt.plot(distances)
    plt.plot(mean, "r--")
    plt.legend(("Distance", "Mean distance (" + str(round(np.mean(distances), 2)) + "')"), loc="upper center")
    plt.grid()
    plt.savefig("data/tmp/dist.png", dpi=600, bbox_inches="tight")
    plt.close()


def plot_pixel_azi_zen(distances, data, type):
    if type == "azim":
        text_label = "Azimuth (º)"
        color_point = "b*"
    if type == "zen":
        text_label = "Zenith (º)"
        color_point = "g*"
    mean = []
    for i in np.arange(0, max(data) + 1, 1):
        mean.append(np.mean(distances))
    plt.ylabel("Pixel distance (arcmin)", fontsize=12)
    plt.xlabel(text_label, fontsize=12)
    plt.plot(data, distances, color_point)
    plt.plot(mean, "r--")
    plt.legend(("Distance", "Mean distance (" + str(round(np.mean(distances), 2)) + "')"), loc="upper center")
    plt.grid()
    plt.savefig("data/tmp/dist_" + type + ".png", dpi=600, bbox_inches="tight")
    plt.close()


def plot_adjust_degree(star_zenit, d_radial, coef):
    d_radial_plot = np.arange(np.min(d_radial), np.max(d_radial), 1)
    plt.plot(d_radial, star_zenit, ".r")
    plt.plot(d_radial_plot, np.polyval(coef, d_radial_plot), "--k")
    plt.xlabel("Radial Distance (arcmin)")
    plt.ylabel("Zenith Angle (º)")
    plt.legend(("Star zenith", "Modeled zenith"), loc="lower right")
    plt.grid()
    plt.savefig("data/tmp/adj_degree.png", dpi=600, bbox_inches="tight")
    plt.close()


def plot_check_azimuth(azim_object, azim_brightness):
    plt.plot(azim_object, azim_brightness, "ob")
    plt.xlabel("Star azimuth (º)")
    plt.ylabel("Brightest point azimuth (º)")
    plt.grid()
    plt.savefig("data/tmp/adj_azim.png", dpi=600, bbox_inches="tight")
    plt.close()


def plot_check_zenith(zen_object, zen_brightness):
    plt.plot(zen_object, zen_brightness, "og")
    plt.xlabel("Star zenith (º)")
    plt.ylabel("Brightest point zenith (º)")
    plt.grid()
    plt.savefig("data/tmp/adj_zen.png", dpi=600, bbox_inches="tight")
    plt.close()
