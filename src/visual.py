import matplotlib.pyplot as plt

def show_fingerprint_grid(img, fft_map, dwt_map, srm_map):
    """
    Displays a 6-panel forensic visualization:
    1. Original image
    2. FFT fingerprint
    3. DWT HH (high-frequency component)
    4. SRM residual map
    5. FFT histogram
    6. DWT histogram (HH band)
    """
    plt.figure(figsize=(16, 10))

    # --- Original Image ---
    plt.subplot(2, 3, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    # --- FFT ---
    plt.subplot(2, 3, 2)
    plt.imshow(fft_map, cmap="inferno")
    plt.title("FFT Fingerprint")
    plt.axis("off")

    # --- DWT HH band (high-frequency) ---
    plt.subplot(2, 3, 3)
    plt.imshow(dwt_map[:, :, 3], cmap="viridis")
    plt.title("DWT – HH (High-Frequency)")
    plt.axis("off")

    # --- SRM residual ---
    plt.subplot(2, 3, 4)
    plt.imshow(srm_map[:, :, 1], cmap="gray")
    plt.title("SRM Residual Map")
    plt.axis("off")

    # --- FFT histogram ---
    plt.subplot(2, 3, 5)
    plt.hist(fft_map.flatten(), bins=40, color="black")
    plt.title("FFT Value Distribution")

    # --- DWT HH histogram ---
    plt.subplot(2, 3, 6)
    plt.hist(dwt_map[:, :, 3].flatten(), bins=40, color="darkblue")
    plt.title("DWT HH Coefficient Distribution")

    plt.tight_layout()
    plt.show()
