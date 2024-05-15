#!/usr/bin/env python3

"""Write a script that reads stdin line
by line and computes metrics
"""
import sys
import signal


# Variables to store metrics
total_file_size = 0
status_counts = {}


# Function to print statistics
def print_statistics():
    print("Total file size:", total_file_size)
    for status_c in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


# Function to handle keyboard interruption
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) == 7:
            try:
                status_code = int(parts[4])
                file_size = int(parts[5])
                total_file_size += file_size
                status_counts[status_c] = status_counts.get(status_c, 0) + 1
            except ValueError:
                pass  # Skip line if status code or file size is not an integer
        if i % 10 == 0:
            print_statistics()
except KeyboardInterrupt:  # Handle keyboard interruption
    print_statistics()
