import cv2
import pywt
import numpy as np

def dwt_fingerprint(img):
    """
    Computes the 2D DWT log-magnitude of an image
    Returns:
        4-channel array: LL, LH, HL, HH - each normalized to [0, 1]
    """
    
    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # db4 gives strong HFreq seperation
    coeffs = pywt.dwt2(gray, 'db4')
    LL, (LH, HL, HH) = coeffs
    
    # Norm all sub-bands
    def norm(c):
        return cv2.normalize(c, None, 0, 1, cv2.NORM_MINMAX)
    
    LL = norm(LL)
    LH = norm(LH)
    HL = norm(HL)
    HH = norm(HH)
    
    # Stack into 4-channel array
    fingerprint = np.stack([LL, LH, HL, HH], axis=-1)
    
    return fingerprint