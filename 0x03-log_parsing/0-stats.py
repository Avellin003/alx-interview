#!/usr/bin/python3

import sys


def parse_line(line):
    """Parse a line into its components."""
    components = line.split()
    if len(components) >= 7:
        ip_address = components[0]
        date = components[2][1:-1]  # Remove square brackets
        status_code = components[-2]
        file_size = int(components[-1])
        return ip_address, date, status_code, file_size
    else:
        return None


def main():
    """Main function to process stdin."""
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()  # Remove leading/trailing whitespace
            line_info = parse_line(line)
            if line_info:
                ip_address, date, status_code, file_size = line_info
                total_size += file_size
                status_counts[status_code] += 1
                line_count += 1

            if line_count == 10:
                print('File size: {}'.format(total_size))
                for key, value in sorted(status_counts.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
                line_count = 0

    except KeyboardInterrupt:
        pass

    finally:
        print('File size: {}'.format(total_size))
        for key, value in sorted(status_counts.items()):
            if value != 0:
                print('{}: {}'.format(key, value))


if __name__ == "__main__":
    main()
