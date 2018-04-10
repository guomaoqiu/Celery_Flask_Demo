#!/bin/bash

#grep "https://fpdl.vimeocdn.com/vimeo-prod-skyfire-std-us" tmp.txt | awk  '{print $2}' | awk -F '"' '{print $2}'

grep "https://fpdl.vimeocdn.com/vimeo-prod-skyfire-std-us" tmp.txt |grep -v "360p" | awk  '{print $2}' | awk -F '"' '{print $2}'  > tmp.log
