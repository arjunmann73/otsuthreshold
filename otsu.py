
import numpy as np
from histogram import histogram

class OtsuThresholder:
    def __init__(self, image):
        self.image = image

    def Otsu(self):
        hist, bins = histogram(self.image.ravel(), 256)
        hist = hist.astype(float)

        weight1 = np.cumsum(hist)
        weight2 = np.cumsum(hist[::-1])[::-1]

        mean1 = np.cumsum(hist * bins) / weight1
        mean2 = (np.cumsum((hist * bins)[::-1]) / weight2[::-1])[::-1]

        variance12 = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

        idx = np.argmax(variance12)
        threshold = bins[:-1][idx]
        return threshold
            
