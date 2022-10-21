#!/usr/bin/env python3

import argparse

import requests

URL_BASE = "http://127.0.0.1"


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int)
    parser.add_argument("--photo-id", "-p", type=int, required=False, default=None)
    args = vars(parser.parse_args())
    return args


def main():
    args = get_args()
    port = args.get("port")
    photo_id = args.get("photo_id")
    if photo_id:
        url = f"{URL_BASE}:{port}/photos/{photo_id}"
    else:
        url = f"{URL_BASE}:{port}/photos"
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f"Unable to establish a connection to the server")
    else:
        print(response.elapsed.total_seconds())


if __name__ == "__main__":
    main()
