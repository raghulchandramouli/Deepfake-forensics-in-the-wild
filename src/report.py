import json

def generate_report(image_path, scores):
    """
    Creates a structured forensic report for a given image.
    Prints it nicely formatted and also returns the dict.
    """

    report = {
        "image_path": image_path,
        "fft_score": round(scores["fft"], 6),
        "dwt_score": round(scores["dwt"], 6),
        "srm_score": round(scores["srm"], 6),
        "combined_score": round(scores["combined"], 6),
        "interpretation": interpret_score(scores["combined"])
    }

    print(json.dumps(report, indent=2))
    return report


def interpret_score(value):
    """
    Simple interpretation helper.
    You can tune thresholds based on your dataset later.
    """

    if value > 0.30:
        return "High likelihood of AI-generated"
    elif value > 0.20:
        return "Possibly AI-generated"
    else:
        return "Likely real image"
