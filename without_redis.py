#!/usr/bin/env python3

import argparse

import requests
import uvicorn
from fastapi import FastAPI, HTTPException

URL = "https://jsonplaceholder.typicode.com/photos"

app = FastAPI()


def get_port() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    port = vars(args)["port"]
    return port


def get_single(id: int):
    response = requests.get(f"{URL}/{id}")
    data = response.json()
    if response.status_code != 200:
        raise HTTPException(status_code=500)
    return data


def get_many():
    response = requests.get(URL)
    data = response.json()
    if response.status_code != 200:
        raise HTTPException(status_code=500)
    return data


@app.get("/photos")
def get_photos():
    photos = get_many()
    return photos


@app.get("/photos/{id}")
def get_photo(id: int):
    photo = get_single(id)
    return photo


if __name__ == "__main__":
    port = get_port()
    uvicorn.run(app, port=port)
