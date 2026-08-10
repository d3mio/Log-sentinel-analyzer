"""
LogSentinel — Production Log Parser and Anomaly Detector
Usage:
    python log_sentinel.py --file app.log --threshold 5
"""

import sys
import re
import argparse
from collections import Counter

def parse_logs(file_path: str, threshold: int):
    print(f"[LogSentinel] Analyzing {file_path} (Alert Threshold: {threshold} errors/min)...")
    error_pattern = re.compile(r"ERROR|CRITICAL|FAIL|EXCEPTION", re.IGNORECASE)
    errors = []
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                if error_pattern.search(line):
                    errors.append(line.strip())
    except FileNotFoundError:
        print(f"[ERROR] Log file not found: {file_path}")
        return

    print(f"\n[SUMMARY] Total error count: {len(errors)}")
    if len(errors) >= threshold:
        print(f"[ALERT] Error threshold exceeded! ({len(errors)} >= {threshold})")
    else:
        print("[OK] Log health normal.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LogSentinel Analyzer")
    parser.add_argument("--file", default="app.log", help="Path to log file")
    parser.add_argument("--threshold", type=int, default=5, help="Alert error threshold")
    args = parser.parse_args()
    parse_logs(args.file, args.threshold)
