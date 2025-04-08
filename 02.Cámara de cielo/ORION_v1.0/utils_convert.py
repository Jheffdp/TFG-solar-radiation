#  Copyright (c) 2020.
#  Juan Carlos Antuña-Sanchez.
#  jcantuna@goa.uva.es
#  Roberto Roman
#  robertor@goa.uva.es
# -*- coding: utf-8 -*-

import csv
import h5py
import numpy as np
import scipy.io


# =============== Convert npy to hdf5 file ===============
def npy_to_h5(npy_file, path_h5_file):
    npy = np.load(npy_file)
    name_file = npy_file.split('.')
    file = name_file[0].split('/')
    hf = h5py.File(path_h5_file + file[len(file) - 1] + ".h5", 'w')
    hf.create_dataset(file[len(file) - 1], data=npy)
    hf.close()


# =============== Convert npy to matlab file ===============
def npy_to_mat(npy_file, path_mat_file):
    npy = np.load(npy_file)
    name_file = npy_file.split('.')
    file = name_file[0].split('/')
    scipy.io.savemat(path_mat_file + file[len(file) - 1] + ".mat", {file[len(file) - 1]: npy.tolist()})


# =============== Convert npy to csv file with selected separator ===============
def npy_to_csv(npy_file, path_csv_file, delimiter):
    npy = np.load(npy_file)
    name_file = npy_file.split('.')
    file = name_file[0].split('/')
    with open(path_csv_file + file[len(file) - 1] + ".csv", 'w', newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(npy)
