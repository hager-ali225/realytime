#!/usr/bin/env python3
import sys
from collections import defaultdict

current_word = None
freq = defaultdict(int)

for line in sys.stdin:
    word, doc = line.strip().split('\t')
    if current_word and word != current_word:
        # طباعة النتيجة للكلمة السابقة
        out = ", ".join([f"{d}:{c}" for d, c in freq.items()])
        print(f"{current_word} -> {out}")
        freq = defaultdict(int)
    current_word = word
    freq[doc] += 1

# آخر كلمة
if current_word:
    out = ", ".join([f"{d}:{c}" for d, c in freq.items()])
    print(f"{current_word} -> {out}")

