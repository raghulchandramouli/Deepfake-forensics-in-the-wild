import cv2
import numpy as np

# A compact set of SRM-inspired high-pass kernels
SRM_FILTERS = [
    # Horizontal residual
    np.array([[0, 0, 0],
              [0, 1, -1],
              [0, 0, 0]]),

    # Vertical residual
    np.array([[0, 0, 0],
              [1, -2, 1],
              [0, 0, 0]]),

    # Diagonal residual
    np.array([[0, 1, 0],
              [0, -2, 1],
              [0, 0, 0]]),
]

def srm_fingerprint(img):
    """
    Applies SRM high-pass filters to extract residual noise fingerprints.
    Returns a stack of residual maps, each normalized to [0,1].
    """
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    maps = []

    for k in SRM_FILTERS:
        r = cv2.filter2D(gray, -1, k)
        r = cv2.normalize(r, None, 0, 1, cv2.NORM_MINMAX)
        maps.append(r)

    return np.stack(maps, axis=-1)  # (H, W, 3)
