#!/usr/bin/python3
import sys
import signal

def print_metrics(signum, frame):
    """Print metrics and reset counters."""
    print("Total file size:", total_size)
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")
    reset_counters()

def reset_counters():
    """Reset counters."""
    global total_size, status_codes
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def process_line(line):
    """Process a line of input."""
    global total_size, status_codes
    try:
        elements = line.split()
        status_code = int(elements[-2])
        file_size = int(elements[-1])
        total_size += file_size
        status_codes[status_code] += 1
    except (ValueError, IndexError):
        pass
