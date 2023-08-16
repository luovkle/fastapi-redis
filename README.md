# fastapi-redis

The purpose of this repository is to show the performance advantages that can be gained by implementing redis even in simple rest api.

## Files

The file **with_redis.py** contains the code of a server made in **fastapi** that implements redis.

The file **without_redis.py** contains the code of a server made in **fastapi** that does not implement redis.

The **run_test.py** file is a utility to measure the seconds it takes for a server to respond to a request.

The **example.sh** file is an example script that shows how a set of tests can be automated using the **run_test.py** utility.

## Requirements

- git
- python3
- docker or redis
- internet connection

## Install dependencies

### Get code

```sh
git clone https://github.com/luovkle/fastapi-redis.git
cd fastapi-redis
```

### Create a virtual environment

```sh
python -m venv .venv
source ./venv/bin/activate
```

### Install packages

```sh
pip install -r requirements.txt
```

## Running redis server

The following example shows how to run the server from docker, however you can run the server installed on the local machine directly.

```sh
docker run --rm --name redis -p 6379:6379 -d redis:alpine
```

## How to run servers

### Granting execution permits

```sh
chmod +x without_redis.py
chmod +x with_redis.py
```

### Running servers

Running the server that does not use redis on port 8080.

```sh
./without_redis.py 8080
```
Running the server using redis on port 8081.

```sh
./with_redis.py 8081
```

### Without execution permissions

Alternatively, the servers can be run without the need to secure execution permissions.

```sh
python without_redis.py 8080
```

```sh
python without_redis.py 8081
```

### Things to consider

The servers have two endpoints:
- /photos
- /ptohos/{photo_id}

Both endpoints use http **get** method.

## How to run tests

### Granting execution permits

```sh
chmod +x run_test.py
```

### Running tests

If you have followed the examples above, the server with port 8080 corresponds to the server that does not use redis and the server with port 8081 corresponds to the server that uses redis.

Note that the first request made to an endpoint on the server using redis will not make any real difference to the server not using redis. The real difference will be reflected in a second request to the same endpoint.

#### Test on port 8080

The following command will run a test on the server **127.0.0.1:8080/photos**.

```sh
./run_test.py 8080
```

The following command will run a test on the server **127.0.0.1:8080/photos/1**.

```sh
./run_test.py 8080 -p 1
```

#### Test on port 8081

The following command will run a test on the server **127.0.0.1:8081/photos**.

```sh
./run_test.py 8081
```

The following command will run a test on the server **127.0.0.1:8081/photos/1**.

```sh
./run_test.py 8081 -p 1
```

### Example automated test

Inside the files of this repository you can find the **example.sh** script. This script is intended to test on 4 different endpoints on both servers.

**example.sh** expects that the servers are already running and that the server that does not use redis runs on port 8080 while the server that does use redis runs on port 8081.

#### Running example

```sh
chmod +x example.sh
./example.sh
```
Expected output for first run.

```txt
>>> Without redis
127.0.0.1:8080/photos
0.432171
127.0.0.1:8080/photos/1
0.330197
127.0.0.1:8080/photos/2
0.238029
127.0.0.1:8080/photos/3
0.229818
-----------------------
>>> With redis
127.0.0.1:8081/photos
0.435041
127.0.0.1:8081/photos/1
0.232723
127.0.0.1:8081/photos/2
0.239102
127.0.0.1:8081/photos/3
0.225132
```

Expected output for a second run.

```txt
>>> Without redis
127.0.0.1:8080/photos
0.615531
127.0.0.1:8080/photos/1
0.389103
127.0.0.1:8080/photos/2
0.461283
127.0.0.1:8080/photos/3
0.339153
-----------------------
>>> With redis
127.0.0.1:8081/photos
0.096654
127.0.0.1:8081/photos/1
0.002529
127.0.0.1:8081/photos/2
0.00229
127.0.0.1:8081/photos/3
0.002277
```
