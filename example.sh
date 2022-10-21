#!/usr/bin/env bash

echo ">>> Without redis"

echo "127.0.0.1:8080/photos"
./run_test.py 8080

echo "127.0.0.1:8080/photos/1"
./run_test.py 8080 -p 1

echo "127.0.0.1:8080/photos/2"
./run_test.py 8080 -p 2

echo "127.0.0.1:8080/photos/3"
./run_test.py 8080 -p 3

echo -e "-----------------------"

echo ">>> With redis"

echo "127.0.0.1:8081/photos"
./run_test.py 8081

echo "127.0.0.1:8081/photos/1"
./run_test.py 8081 -p 1

echo "127.0.0.1:8081/photos/2"
./run_test.py 8081 -p 2

echo "127.0.0.1:8081/photos/3"
./run_test.py 8081 -p 3
