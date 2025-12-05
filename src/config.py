import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SAMPLE_IMAGES_DIR = os.path.join(BASE_DIR, 'images')

# --- Sample Image Subdirectories ---
REAL_DIR = os.path.join(SAMPLE_IMAGES_DIR, 'real')
FAKE_DIR = os.path.join(SAMPLE_IMAGES_DIR, 'fake')