#!/bin/bash
for filename in experiments/*; do
  nohup python3 -u run.py "$filename" >> log &
done