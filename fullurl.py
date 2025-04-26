#!/usr/bin/env python3

import sys
import argparse
from urllib.parse import urljoin

def main():
    parser = argparse.ArgumentParser(description="Expand relative URLs into full URLs based on a base URL.")
    parser.add_argument("-u", "--url", required=True, help="Base URL to resolve relative links against.")
    args = parser.parse_args()

    base_url = args.url.strip()
    absolute_schemes = ("http://", "https://", "file://", "data:", "ftp://", "chrome-extension://")

    stdin = sys.stdin.read().splitlines()
    for line in stdin:
        link = line.strip()
        if not link:
            continue
        if link.startswith(absolute_schemes):
            print(link)
        else:
            print(urljoin(base_url, link))

if __name__ == "__main__":
    main()
