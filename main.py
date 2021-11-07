from PIL import Image, ImageOps
import numpy as np
from numpy import asarray
from otsu import OtsuThresholder

if __name__ == "__main__":
    image = Image.open("images/image1.png")
    image = ImageOps.grayscale(image)
    image = asarray(image)

    Otsu = OtsuThresholder(image)
    threshold = Otsu.Otsu()

    binary = image <= threshold
    binary = binary.astype(int)

    print(len(binary[0]))
    
    
    binaryImage= Image.fromarray(binary*255, "L")
   
    binaryImage.show()
    

    



    