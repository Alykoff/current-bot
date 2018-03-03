#!/bin/bash
TOKEN=$(cat SECRET)
nohup python3 server.py $TOKEN

