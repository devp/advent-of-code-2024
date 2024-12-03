#!/usr/bin/env python3

import sys
import subprocess
from datetime import date


def todays_day() -> int:
    return date.today().day


def download_day(day: int):
    url = f"https://adventofcode.com/2024/day/{day}"
    subprocess.run(['curl', '-o', f"{day}.html", url])


day: int = int(sys.argv[1]) if len(sys.argv) >= 2 else todays_day()
download_day(day)
