#!/usr/bin/python3
'''reads line and computes metrics'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_s = 0
counter = 0

try:
    for lin in sys.stdin:
        line_l = lin.split(" ")
        if len(line_l) > 4:
            code = line_l[-2]
            size = int(line_l[-1])
            if code in cache.keys():
                cache[code] += 1
            total_s += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_s))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_s))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
