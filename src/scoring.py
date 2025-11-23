import numpy as np

def score_fft(fft_map):
    """
    FFT often has strong periodic peaks in AI images.
    A higher standard deviation generally indicates synthetic patterns.
    """
    return float(np.std(fft_map))


def score_dwt(dwt_map):
    """
    DWT-HH band captures high-frequency noise.
    AI images often show abnormal HH energy levels.
    """
    hh_band = dwt_map[:, :, 3]  # HH (high-high band)
    return float(np.mean(np.abs(hh_band)))


def score_srm(srm_map):
    """
    SRM residuals become too uniform or too chaotic in fake images.
    """
    return float(np.std(srm_map))


def combined_score(fft_score, dwt_score, srm_score):
    """
    Weighted sum prioritizing FFT fingerprints.
    """
    return (
        0.60 * fft_score +   # Highest weight
        0.25 * dwt_score +   # Medium weight
        0.15 * srm_score     # Smallest weight
    )
