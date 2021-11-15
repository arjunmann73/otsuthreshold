from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
from otsu import OtsuThresholder
import matplotlib.pyplot as plt
from skimage.filters import threshold_local
import pytesseract
import logging
import cv2 as cv
import os
logging.basicConfig(filename="logs/logs2.log", filemode="w", level=logging.INFO, format='%(message)s')


def plotImages(image, binary):
    fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
    ax = axes.ravel()
    ax[0] = plt.subplot(1, 3, 1, adjustable='box')
    ax[1] = plt.subplot(1, 3, 2)
    ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0], adjustable='box')

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')
    ax[0].axis('off')

    ax[1].hist(image.ravel(), bins=256)
    ax[1].set_title('Histogram')
    ax[1].axvline(threshold, color='r')

    ax[2].imshow(binary, cmap=plt.cm.gray)
    ax[2].set_title('Thresholded')
    ax[2].axis('off')

    plt.show()

if __name__ == "__main__":
    imageName = "image2.png"
    image = Image.open("images/" + imageName)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    imageOriginal = asarray(image)
    logging.info("Basic image:")
    text = pytesseract.image_to_string(image)
    logging.info(text)
    
    image = ImageOps.grayscale(image)
    image = asarray(image)
    logging.info("Grayscale image image:")
    text = pytesseract.image_to_string(image)
    logging.info(text)

    block_size = 35
    adaptive_thresh = threshold_local(image, block_size, offset=10)
    binary_adaptive = image > adaptive_thresh

    logging.info("Addaptive threshold binarization image:")
    text = pytesseract.image_to_string(binary_adaptive)
    logging.info(text)
    
    Otsu = OtsuThresholder(image)
    threshold = Otsu.Otsu()
    binary = image > threshold
    binary = binary.astype(int)
    binary = binary * 255

    if not os.path.isfile("images/results/otsu1.png") and imageName == "image1.png":
        cv.imwrite("images/results/otsu1.png", binary)
    if not os.path.isfile("images/results/otsu2.png") and imageName == "image2.png":
        cv.imwrite("images/results/otsu2.png", binary)
    
    if imageName == "image1.png":
        imageOtsu = cv.imread("images/results/otsu1.png", 0)
    else:
        imageOtsu = cv.imread("images/results/otsu2.png", 0)

    logging.info("Otsu threshold binarization image:")
    text = pytesseract.image_to_string(imageOtsu)
    logging.info(text)

    plotImages(image, binary)
    plotImages(image, binary_adaptive)




    
    

    



    