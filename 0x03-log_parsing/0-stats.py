#!/usr/bin/python3
'''reads line and computes metrics'''

import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_parts = line.split(" ")
        if len(line_parts) > 4:
            code = line_parts[-2]
            try:
                size = int(line_parts[-1])
            except ValueError:
                continue  # Skip lines with invalid size
            if code in cache:
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
            total_size = 0
            cache = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}
            counter = 0

    # Print remaining stats if not exactly 10 lines
    if counter > 0:
        print('File size: {}'.format(total_size))
        for key, value in sorted(cache.items()):
            if value != 0:
                print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    pass

