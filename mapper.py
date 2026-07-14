#!/usr/bin/env python3
import sys
import string
import os

# اقرأ stopwords
stopwords = set(open("stopwords.txt").read().splitlines())

# خد اسم الملف من environment variable الخاصة بالـ Hadoop Streaming
filename = os.environ.get('map_input_file', 'unknown_file')
filename = os.path.basename(filename)  # خلي الاسم بس من غير المسار

for line in sys.stdin:
    line = line.strip().lower()
    line = line.translate(str.maketrans("", "", string.punctuation))
    for word in line.split():
        if word and word not in stopwords:
            print(f"{word}\t{filename}")
