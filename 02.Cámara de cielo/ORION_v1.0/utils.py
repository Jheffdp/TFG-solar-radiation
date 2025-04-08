#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

import cmath
import datetime as dt
import os
import cv2
import ephem
import ephem.stars
import numpy as np
from matplotlib import image
import utils_plots

np.seterr(divide="warn", invalid="warn")

"""Calculate distance between pixels and select the most near pixel
    Receive:
        azimut_input : float
            Azimuth to locate
        zenit_input : float
            Zenith to locate
        azimut_matrix : numpy matrix
            Azimuth calibration matrix
        zenit:matrix : numpy matrix
            Zenith calibration matrix
    Return:
        pixel_coordinates : tuple
            x, y position for pixel to locate
"""


def select_pixel(azimut_input, zenit_input, azimut_matrix, zenit_matrix):
    dista = haversine_distance(
        90 - zenit_matrix, azimut_matrix, 90 - zenit_input, azimut_input
    )
    pixel_coordinates = np.where(dista == np.min(dista))
    pixel_coordinates = (pixel_coordinates[1][0], pixel_coordinates[0][0])

    return pixel_coordinates


def haversine_distance(lat1, lon1, lat2, lon2):
    r = 1
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = (
        np.sin(delta_phi / 2) ** 2
        + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    )
    res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return res


"""Get data for selected star
    Receive:
        name : string
            Star name
        date_ : datetime
            Date and time 
        lon_ : float
            Longitude
        lat_ : float
            Latitude
        elev_ : float
            Height above sea level
    Return:
        star_zenith_ : float
            Star zenith
        star_azim_ : float
            Star azimuth  
"""


def get_star(name, date_, lon_, lat_, elev_):
    star = ephem.star(name)
    location = ephem.Observer()
    location.lon = str(lon_)
    location.lat = str(lat_)
    location.elevation = elev_
    location.date = date_
    star.compute(location)
    star_zenith_ = 90 - np.degrees(star.alt)
    star_azim_ = np.mod(90 + np.degrees(star.az), 360) - 90
    return star_zenith_, star_azim_


"""Get datetime for image file
    Receive:
        file_img : string
            File image filename with format "id_date(YMD)_time(HHMM).extension"
    Return:
        datetime_img : datetime
            Date and time for image file
"""


def get_date_img(file_img):
    try:
        name, ext = file_img.split(".")
        if ext in ("jpg", "png"):
            try:
                id_img, date_img, time_img = name.split("_")
                datetime_img = dt.datetime(
                    int(date_img[:4]),
                    int(date_img[4:6]),
                    int(date_img[6:8]),
                    int(time_img[:2]),
                    int(time_img[2:4]),
                    0,
                )
                return datetime_img
            except ValueError:
                return 0
        else:
            return 0
    except ValueError:
        return 0


"""Read and concatenate npy star data files for calculate center and generate calibration matrix
    Receive:
        files : string array
            One or list files path
    Return:
        all_data : numpy array
            Array with all data
"""


def read_files(files):
    if files != []:

        all_data = []
        count = 0

        for file in files:
            if file == "":
                continue
            file_name = file.split("/")
            ext = file_name[len(file_name) - 1].split(".")

            if ext[1] == "npy":
                data = np.load(file)
                if len(data) == 0:
                    continue
                if np.shape(data)[1] == 4:
                    if count == 0:
                        all_data = data
                    if count > 0:
                        all_data = np.concatenate((all_data, data), axis=0)
                    count += 1
                else:
                    continue
        return all_data
    return []


"""Get file list for images path
    Receive:
        path : string
            Path files
    Return:
        files : string list
            List with the filenames sorted
"""


def read_img_path(path):
    lstDir = os.listdir(path)
    lst_files = []
    for file in sorted(lstDir):
        if get_date_img(file) != 0:
            lst_files.append(file)
    return lst_files


def image_size(path):
    images = read_img_path(path)
    img = image.imread(path + images[0])
    size = img.shape
    return size[0], size[1]


def initial_matrix(img_h, img_w, inital_gap, extreme_zen):
    col_center = np.floor(img_h / 2) + 0.5
    row_center = np.floor(img_w / 2) + 0.5

    d_radial2 = img_h - row_center
    slope = extreme_zen / d_radial2

    y_matrix = np.zeros((img_h, img_w))
    x_matrix = np.zeros((img_h, img_w))

    for m in np.arange(0, img_h, 1):
        for n in np.arange(0, img_w, 1):
            x = n - col_center
            y = row_center - m
            y_matrix[m, n] = y
            x_matrix[m, n] = x

    d_radial_matrix = np.sqrt((x_matrix * x_matrix) + (y_matrix * y_matrix))

    sza = d_radial_matrix * slope
    ratio = y_matrix / x_matrix
    angle = np.rad2deg(np.arctan(ratio))

    angle = np.where(x_matrix < 0, (angle + 90), angle)
    angle = np.where(x_matrix > 0, (angle + 270), angle)

    angle_2 = angle - inital_gap

    angle_2 = np.where(angle_2 < 0, (angle_2 + 360), angle_2)
    angle_2 = np.where(angle_2 > 360, (angle_2 - 360), angle_2)

    azimut = angle_2
    zenit = sza
    return azimut, zenit


def read_all_stars():
    star_list = []
    for star in ephem.stars.db.split("\n"):
        star_list.append(star.split(",")[0])
    return sorted(star_list)


def calculate_matrix(col_center, row_center, img_h, img_w, data_in, degree, flip):
    zenlimit = -200
    data = data_in[data_in[:, 2] > zenlimit]
    col = np.array(data[:, 0])
    row = np.array(data[:, 1])
    ZenStar = np.array(data[:, 2])
    AziStar = np.array(data[:, 3])

    seno = col_center - col
    coseno = row_center - row
    d_radial = np.sqrt(seno ** 2 + coseno ** 2)
    coef = np.polyfit(d_radial, ZenStar, degree)
    angulo = np.rad2deg(np.arctan2(seno, coseno))
    AziStar = np.where(AziStar > 180, (AziStar - 360), AziStar)
    AziStar = np.where(AziStar < -180, (AziStar + 360), AziStar)
    angulo = np.where(angulo > 180, (angulo - 360), angulo)
    angulo = np.where(angulo < -180, (angulo + 360), angulo)
    zenlimit = 20
    AziStar2 = AziStar[ZenStar > zenlimit]
    angulo2 = angulo[ZenStar > zenlimit]
    mini2 = np.where(AziStar2 == np.min(AziStar2))
    angulo2_min = angulo2[mini2]
    AziStar2 = AziStar2[
        np.logical_or((angulo2 > angulo2_min + 1), (angulo2 < angulo2_min - 1))
    ]
    angulo2 = angulo2[
        np.logical_or((angulo2 > angulo2_min + 1), (angulo2 < angulo2_min - 1))
    ]

    angulo2 = np.where(angulo2 < angulo2_min, angulo2 + 360, angulo2)
    dif = angulo2 - AziStar2

    ecAzi = np.polyfit(AziStar2, angulo2, 1)
    desfase = ecAzi[1]

    y_matrix = np.zeros((img_h, img_w))
    x_matrix = np.zeros((img_h, img_w))
    for m in np.arange(0, img_h):
        for n in np.arange(0, img_w):
            x = n - col_center
            y = row_center - m
            y_matrix[m, n] = y
            x_matrix[m, n] = x

    d_radial_matrix = np.sqrt((x_matrix * x_matrix) + (y_matrix * y_matrix))
    if degree == 1:
        sza = d_radial_matrix * coef[0] + coef[1]
    if degree == 2:
        sza = (
            d_radial_matrix * d_radial_matrix * coef[0]
            + d_radial_matrix * coef[1]
            + coef[2]
        )
    if degree == 3:
        sza = (
            d_radial_matrix * d_radial_matrix * d_radial_matrix * coef[0]
            + d_radial_matrix * d_radial_matrix * coef[1]
            + coef[2] * d_radial_matrix
            + coef[3]
        )

    utils_plots.plot_adjust_degree(star_zenit=ZenStar, d_radial=d_radial, coef=coef)

    ratio = y_matrix / x_matrix
    angle = np.rad2deg(np.arctan(ratio))

    angle = np.where(x_matrix < 0, (angle + 90), angle)
    angle = np.where(x_matrix > 0, (angle + 270), angle)

    angle_2 = angle - desfase

    angle_2 = np.where(angle_2 < 0, (angle_2 + 360), angle_2)
    angle_2 = np.where(angle_2 > 360, (angle_2 - 360), angle_2)

    if flip == 0:
        azimut = angle_2
        zenit = sza
    else:
        if flip == 1:
            azimut = np.flip(angle_2, 0)
            zenit = np.flip(sza, 0)
        if flip == 2:
            azimut = np.flip(angle_2, 1)
            zenit = np.flip(sza, 1)
        if flip == 3:
            azimut = np.flip(angle_2)
            zenit = np.flip(sza)

    utils_plots.plot_matrix(data=azimut, title="Azimuth matrix", type="azimut")
    utils_plots.plot_matrix(data=zenit, title="Zenith matrix", type="zenit")
    shift_north = desfase
    if desfase > 180:
        shift_north = desfase - 360
    if desfase <= -180:
        shift_north = desfase + 360

    return azimut, zenit, shift_north


"""Circular standard deviation of angle data(default to degree)
0 <= std. The directional standard deviation
"""


def circular_std(angles, deg=True):
    a = np.deg2rad(angles) if deg else np.array(angles)
    angles_complex = np.frompyfunc(cmath.exp, 1, 1)(a * 1j)
    r = abs(angles_complex.sum()) / len(angles)
    std = np.sqrt(-2 * np.log(r))
    return round(np.rad2deg(std) if deg else std, 7)


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


def max_bright_point(plus_width, plus_height, coord, image_data):
    imCrop = image_data[
        int(coord[1]) - plus_width : int(coord[1]) + plus_width,
        int(coord[0] - plus_height) : int(coord[0] + plus_height),
    ]
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imCrop)
    coord = (maxLoc[0] + (coord[0] - plus_height), maxLoc[1] + coord[1] - plus_width)
    return coord


# ========== Read default configuration ==========
def read_default_input():
    file = "data/default_input.dat"
    if os.path.isfile(file):
        file = open(file, "r")
        line = file.read()
        if line != "":
            (
                lat,
                lon,
                elev,
                img_path,
                height,
                width,
                azimut_matrix,
                zenit_matrix,
            ) = line.split(";")
        else:
            lat = 0
            lon = 0
            elev = 0
            img_path = ""
            height = 0
            width = 0
            azimut_matrix = ""
            zenit_matrix = ""
        file.close()
        return (
            float(lat),
            float(lon),
            float(elev),
            str(img_path),
            int(height),
            int(width),
            str(azimut_matrix),
            str(zenit_matrix),
        )
    return 0, 0, 0, "", 0, 0, "", ""


# ========== Calculate pixel distance ==========
def pixel_distance(x1, y1, x2, y2, azimut_mat, zenit_mat):
    dist = haversine_distance(
        azimut_mat[y1, x1],
        zenit_mat[y1, x1],
        azimut_mat[y2, x2],
        zenit_mat[y2, x2]
    )
    return np.degrees(dist) * 60


def even_divide(lst, num_piece=4):
    return [
        [lst[i] for i in range(len(lst)) if (i % num_piece) == r]
        for r in range(num_piece)
    ]
