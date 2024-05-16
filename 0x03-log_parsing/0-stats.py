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
<status code>, <file size>]
"""

import sys

# Store the count of all status codes in a dictionary
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                 '404': 0, '405': 0, '500': 0}

tsize = 0
line_count = 0  # keep count of the number of lines processed

try:
    for line in sys.stdin:
        line_info = line.split(" ")

        if len(line_info) > 4:
            status_code = line_info[-2]
            file_size = int(line_info[-1])

            # Check if the status code exists in the dictionary and
            # increment its count
            if status_code in status_counts.keys():
                status_counts[status_code] += 1

            # Update tsize
            tsize += file_size

            # Update count of lines
            line_count += 1

        if line_count == 10:
            line_count = 0  # Reset count
            print('File size: {}'.format(tsize))

            # Print out status code counts
            for key, value in sorted(status_counts.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(tsize))
    for key, value in sorted(status_counts.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
