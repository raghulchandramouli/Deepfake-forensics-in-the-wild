import cv2, os

def load_image(path):
    """
    Loads an images from disk
    """
    
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Image not found at path: {path}")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def list_images(folder):
    """
    Returns a list of abs path
    """
    
    exts = (".jpg", ".jpeg", ".png")
    files = []
    
    for f in os.listdir(folder):
        if f.lower().endswith(exts):
            files.append(os.path.join(folder, f))
            
    return files