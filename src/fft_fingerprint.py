import cv2
import numpy as np

def fft_fingerprint(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # FFT
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    
    # Log magnitude
    magnitude = 20 * np.log(np.abs(fshift) + 1e-8)
    
    # Convert to float32 and normalize to [0, 1]
    magnitude = magnitude.astype(np.float32)
    magnitude = cv2.normalize(magnitude, None, 0, 1, cv2.NORM_MINMAX)
    
    return magnitude
