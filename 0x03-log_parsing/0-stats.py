#!/usr/bin/python3
"""alx-interview/log_parsing"""

import sys

if __name__ == '__main__':

    fsize, counter = 0, 0
    cds = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status = {k: 0 for k in cds}

    def print_status(status: dict, fsize: int) -> None:
        print("File size: {:d}".format(fsize))
        for k, v in sorted(status.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for lne in sys.stdin:
            counter += 1
            data = lne.split()
            try:
                scode = data[-2]
                if scode in status:
                    status[scode] += 1
            except BaseException:
                pass
            try:
                fsize += int(data[-1])
            except BaseException:
                pass
            if counter % 10 == 0:
                print_status(status, fsize)
        print_status(status, fsize)
    except KeyboardInterrupt:
        print_status(status, fsize)
        raise
