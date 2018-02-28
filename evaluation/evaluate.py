#!/usr/bin/env python

import PIL.Image
import errno
import glob
import numpy as np
import os
import pickle
import skimage.measure
import sys

input_path = sys.argv[1]
ref_path = os.path.join(input_path, 'ref')
res_path = os.path.join(input_path, 'res')
output_path = sys.argv[2]

try:
    os.makedirs(output_path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

mse = []
psnr = []
ssim = []

for fp in glob.glob(os.path.join(ref_path, '*.jpg')):
    try:
        mse.append(0)
        psnr.append(0)
        ssim.append(0)

        y = np.array(PIL.Image.open(fp).convert('L')) / 255
        y_hat = np.array(PIL.Image.open(os.path.join(res_path, os.path.split(fp)[1])).convert('L').resize((275, 400))) / 255

        mse.append(skimage.measure.compare_mse(y, y_hat))
        psnr.append(skimage.measure.compare_psnr(y, y_hat))
        ssim.append(skimage.measure.compare_ssim(y, y_hat))
    except:
        pass

with open(os.path.join(output_path, 'scores.txt'), 'w') as f:
    f.write('mse: {}\npsnr: {}\nssim: {}'.format(np.mean(mse), np.mean(psnr), np.mean(ssim)))
