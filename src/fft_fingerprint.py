import numpy as np
import cv2

def fft_fingerprint(img):
    
    """
    Computes the 2D fft log-magnitude of an images
    
    Returns:
        normalized freq [0, 1]
    """
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # FFT
    f = np.fft.fft2(gray)
    fshift = np.fft.fftshift(f)
    
    # Log magnitude
    magnitude = 20 * np.log(np.abs(fshift) + 1e-8)
    
    # Normalize to [0, 1]
    magnitude = cv2.magnitude(magnitude, None, 0, 1, cv2.NORM_MINMAX)
    
    return magnitude