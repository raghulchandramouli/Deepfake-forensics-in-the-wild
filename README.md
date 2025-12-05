# Deepfake Forensics in the Wild

A model-free forensic analysis toolkit for detecting AI-generated images using frequency domain analysis.

## Overview

This project implements three complementary forensic techniques to detect deepfakes and AI-generated images:

- **FFT (Fast Fourier Transform)**: Detects periodic artifacts in the frequency domain
- **DWT (Discrete Wavelet Transform)**: Analyzes high-frequency anomalies using Daubechies-4 wavelets
- **SRM (Spatial Rich Models)**: Extracts residual noise patterns using high-pass filters

## Project Structure

```
Deepfake-Forensics-in-the-wild/
├── src/                      # Source modules
│   ├── __init__.py          # Package exports
│   ├── config.py            # Configuration and paths
│   ├── utils_io.py          # Image loading utilities
│   ├── fft_fingerprint.py   # FFT analysis
│   ├── dwt_fingerprint.py   # DWT analysis
│   ├── srm_filter.py        # SRM filters
│   ├── scoring.py           # Scoring algorithms
│   ├── report.py            # Report generation
│   └── visual.py            # Visualization tools
├── nbs/                     # Notebooks
│   ├── forensics.ipynb      # Main analysis notebook
│   └── run_notebook.py      # Automated execution script
└── images/                  # Sample images
    ├── real/                # Real photographs
    └── fake/                # AI-generated images
```

## Installation

```bash
# Install dependencies
pip install opencv-python pywt numpy matplotlib jupyter papermill
```

## Usage

### Option 1: Jupyter Notebook (Interactive)

```bash
# Launch Jupyter
jupyter notebook

# Open nbs/forensics.ipynb and run cells
```

### Option 2: Automated Execution

```bash
# Run the entire pipeline
python nbs/run_notebook.py
```

## Adding Sample Images

1. Place real photographs in `images/real/`
2. Place AI-generated/fake images in `images/fake/`
3. Supported formats: `.jpg`, `.jpeg`, `.png`

The notebook will automatically process all images in both directories.

## How It Works

### 1. Fingerprint Extraction
Each image is analyzed using three forensic filters:
- **FFT**: Converts to frequency domain and computes log-magnitude spectrum
- **DWT**: Decomposes into 4 sub-bands (LL, LH, HL, HH) using db4 wavelets
- **SRM**: Applies high-pass residual filters to extract noise patterns

### 2. Scoring
Each fingerprint is scored based on statistical properties:
- **FFT Score**: Standard deviation of frequency spectrum (higher = more synthetic)
- **DWT Score**: Mean energy in HH band (abnormal values indicate AI generation)
- **SRM Score**: Standard deviation of residuals (too uniform or chaotic = fake)

### 3. Combined Score
Weighted combination: `0.60 × FFT + 0.25 × DWT + 0.15 × SRM`

### 4. Interpretation
- **> 0.30**: High likelihood of AI-generated
- **0.20 - 0.30**: Possibly AI-generated
- **< 0.20**: Likely real image

## Example Output

The notebook generates:
- 6-panel forensic visualizations for each image
- Detailed JSON reports with scores
- Comparative analysis between real and fake images
- Bar charts showing score differences

## Limitations

- Model-free approach (no ML training required)
- Works best on uncompressed or lightly compressed images
- Thresholds may need tuning for specific datasets
- Not robust against adversarial attacks

## Future Enhancements

- [ ] Add PRNU (Photo Response Non-Uniformity) analysis
- [ ] Implement ELA (Error Level Analysis)
- [ ] Support for video deepfake detection
- [ ] Web interface for easy testing
- [ ] Batch processing CLI tool

## References

- Fridrich, J. (2009). "Digital Image Forensics"
- Cozzolino, D. et al. (2018). "Forensic Analysis of Deep Fakes"
- Spatial Rich Models for steganalysis

## License

MIT License - Feel free to use and modify for research and educational purposes.
