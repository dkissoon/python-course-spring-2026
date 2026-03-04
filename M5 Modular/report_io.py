"""
report_io.py

Purpose:
This module handles reading and writing budget reports to disk.

How it interacts with the program:
- main.py generates a report string and calls save_report()
- main.py can optionally call load_report() to view past reports
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional


def ensure_reports_dir(folder_name: str = "reports") -> Path:
    """
    Ensure the reports folder exists and return the folder path.
    """
    reports_dir = Path(folder_name)
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir


def save_report(report_text: str, filename: str, folder_name: str = "reports") -> Path:
    """
    Save a report to a file and return the full path.

    Args:
        report_text: The report content to write.
        filename: The file name (example: "budget_report_2026-02-28.txt")
        folder_name: Folder where reports are stored.

    Returns:
        The path to the saved report file.
    """
    reports_dir = ensure_reports_dir(folder_name)
    path = reports_dir / filename
    path.write_text(report_text, encoding="utf-8")
    return path


def load_report(filename: str, folder_name: str = "reports") -> Optional[str]:
    """
    Load a report by filename. Returns None if not found.
    """
    path = Path(folder_name) / filename
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")