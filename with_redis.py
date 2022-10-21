#!/usr/bin/env python3

import argparse
import json

import redis
import requests
import uvicorn
from fastapi import FastAPI, HTTPException

URL = "https://jsonplaceholder.typicode.com/photos"
DEFAULT_EXPIRATION = 60 * 60  # 1 hour

r = redis.Redis()

app = FastAPI()


def get_port():
    parser = argparse.ArgumentParser()
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    port = vars(args)["port"]
    return port


def get_single(id: str):
    data = r.get(id)
    if data:
        data = json.loads(data)
    elif not data:
        response = requests.get(f"{URL}/{id}")
        if response.status_code != 200:
            raise HTTPException(status_code=500)
        data = response.json()
        data_str = json.dumps(data)
        r.setex(id, DEFAULT_EXPIRATION, data_str)
    return data


def get_many():
    data = r.get("photos")
    if data:
        data = json.loads(data)
    if not data:
        response = requests.get(URL)
        if response.status_code != 200:
            raise HTTPException(status_code=500)
        data = response.json()
        data_str = json.dumps(data)
        r.setex("photos", DEFAULT_EXPIRATION, data_str)
    return data


@app.get("/photos")
def get_photos():
    photos = get_many()
    return photos


@app.get("/photos/{id}")
def get_photo(id: str):
    photo = get_single(id)
    return photo


if __name__ == "__main__":
    port = get_port()
    uvicorn.run(app, port=port)
