#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            tokens = line.split()
            if len(tokens) > 2:
                total_size += int(tokens[-1])
                status_code = tokens[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1

            count += 1
            if count == 10:
                print_metrics(total_size, status_codes)
                count = 0

    except KeyboardInterrupt:
        pass

    print_metrics(total_size, status_codes)

if __name__ == "__main__":
    main()
