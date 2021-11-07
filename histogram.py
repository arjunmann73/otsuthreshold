import numpy as np

def histogram(image, nbins=256):
    if np.issubdtype(image.dtype, np.integer):
        offset = 0
        image_min = np.min(image)
        if image_min < 0:
            offset = image_min
            image_range = np.max(image).astype(np.int64) - image_min
            # get smallest dtype that can hold both minimum and offset maximum
            offset_dtype = np.promote_types(np.min_scalar_type(image_range),
                                            np.min_scalar_type(image_min))
            if image.dtype != offset_dtype:
                # prevent overflow errors when offsetting
                image = image.astype(offset_dtype)
            image = image - offset
        hist = np.bincount(image.ravel())
        bin_centers = np.arange(len(hist)) + offset

        # clip histogram to start with a non-zero bin
        idx = np.nonzero(hist)[0][0]
        return hist[idx:], bin_centers[idx:]
    else:
        hist, bin_edges = np.histogram(image.flat, bins=nbins)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.
        return hist, bin_centers