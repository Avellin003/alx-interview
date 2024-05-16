#!/usr/bin/python3
"""Script to calculate metrics by reading stdin line by line:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (line is skipped if not in this format)
After every 10 lines and/or a keyboard interruption (CTRL + C),
prints statistics:
Total file size: File size: <tsize>
where <tsize> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405, and 500
if a status code doesn’t appear or is not an integer,
no output for that status code
format: <status code>: <number>
status codes printed in ascending order

line_info = [<IP Address>, -, [<date>], "GET /projects/260 HTTP/1.1",
<status code>, <file size>]"""

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
