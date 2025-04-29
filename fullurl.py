#!/usr/bin/env python3

import sys
import argparse
from urllib.parse import urljoin, urlparse

def main():
    parser = argparse.ArgumentParser(description="Expand relative URLs based on a base URL.")
    parser.add_argument("-u", "--url", required=True, help="Base URL to resolve relative links against.")
    args = parser.parse_args()

    base_url = args.url.strip()
    absolute_schemes = ("http://", "https://", "file://", "data:", "ftp://", "chrome-extension://")

    parsed_base = urlparse(base_url)
    site_root = f"{parsed_base.scheme}://{parsed_base.netloc}/"

    stdin = sys.stdin.read().splitlines()
    for line in stdin:
        link = line.strip()
        if not link:
            continue
        if link.startswith(absolute_schemes):
            print(link)
        elif link.startswith("./"):
            # Link relative to the base URL's folder
            print(urljoin(base_url, link))
        else:
            # Link relative to root
            print(urljoin(site_root, link))

if __name__ == "__main__":
    main()
