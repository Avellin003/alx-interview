#!/usr/bin/python3
"""alx-interview/log_parsing"""

import sys


class LogParser:
    def __init__(self):
        self.filesize = 0
        self.count = 0
        self.codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
        self.stats = {k: 0 for k in self.codes}

    def print_stats(self):
        print("File size: {:d}".format(self.filesize))
        for k, v in sorted(self.stats.items()):
            if v:
                print("{}: {}".format(k, v))

    def parse_logs(self):
        try:
            for line in sys.stdin:
                self.count += 1
                data = line.split()
                try:
                    status_code = data[-2]
                    if status_code in self.stats:
                        self.stats[status_code] += 1
                except Exception:
                    pass
                try:
                    self.filesize += int(data[-1])
                except Exception:
                    pass
                if self.count % 10 == 0:
                    self.print_stats()
            self.print_stats()
        except KeyboardInterrupt:
            self.print_stats()
            raise


if __name__ == '__main__':
    parser = LogParser()
    parser.parse_logs()
