# Otsuthreshold
Otsu thresholding algorithm for converting grayscale images to binary images. We compare this algorithm with adaptive thresholding for OCR functionalities.

OCR is performed using Tesseract, do install Tesseract to run these files. 

## 1.1. Otsu thresholding applied to Image 1
![](images/results/otsucompare1.png)

## 1.2. Adaptive thresholding applied to Image 1
![](images/results/adaptivecompare1.png)

## 2.1. Otsu thresholding applied to Image 2
![](images/results/otsucompare2.png)

## 2.2. Adaptive thresholding applied to Image 2
![](images/results/adaptivecompare2.png)

## 3.1. Otsu thresholded binary image1
![](images/results/otsu1.png)

## 3.2. Otsu thresholded binary image2
![](images/results/otsu2.png)


OCR results are generated through tesseract which takes the thresholded binary image as an input:
|  | Otsu threshold | Adaptive threshold |
| --- | --- | --- |
| Image1 | Parking You may park anywhere on the ctking. Keep in mind the carpool hours and peri afternoon Under School Age Children:While we love inappropriate to have them on campus @ . that they may be invited or can accompany J you adhere to our _policy for the benefit of  | Parking: You may park anywhere on the campus where there are no signs prohibiting par-king. Keep in mind the carpool hours and park accordingly so you do not get blocked in the afternoon Under Schoo! Age Children.While we love the younger children, it can be disruptive and inappropriate to have them on campus during schoo! hours. There may be special times that they may be invited or can accompany a parent volunteer, but otherwise we ask that you adhere to our ~� policy for the benefit of the students and staff. |
| Image2 | Sonnet for lens | Sonnet for Lena O deer Lena, your benuty isso ens Vn in barcl wanetimes ta describe it, [nat Lehought the entire world T wankd lapresa TE only sour portrait [ enukd compress, Atlus! Firat when [tried to use �Q nd that your checks belong to only you. y hair coulaion @ thotuud Haws Tfard to imatth #ith suins of discrete cositics. And fur your Lips, setsitial and tartial Thirteen Craye fount aot the proper fractal. Auel while these setbacks are all ap Diainht have fice them with lacks here or there Bt whoa dilters tack apackle dro Durag all this, VL past dipitire. Dee per vig yi oven Dsaid, then Coltliaeat |
