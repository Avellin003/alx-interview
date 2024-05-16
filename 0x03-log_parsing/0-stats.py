#!/usr/bin/python3
'''reads stdin and prints key metrics'''


import sys

cached = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
size = 0
counter = 0

try:
    for i in sys.stdin:
        lllist = i.split(" ")
        if len(lllist) > 4:
            cmd = lllist[-2]
            s = int(lllist[-1])
            if cmd in cached.keys():
                cached[cmd] += 1
            size += s
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(size))
            for key, value in sorted(cached.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(size))
    for key, value in sorted(cached.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
