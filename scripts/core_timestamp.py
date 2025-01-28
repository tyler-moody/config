#!/opt/qumulo/toolchain/bin/python

import argparse
import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Print a human-readable representation of the Unix epoch timestamp in a qfsd core filename"
    )
    parser.add_argument("filename")
    args = parser.parse_args()
    filename = args.filename
    timestamp = filename.split("-")[1]
    print(datetime.datetime.fromtimestamp(int(timestamp)))
