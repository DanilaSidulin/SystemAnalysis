# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1nqmu5QDSUfsUPMrwyQdLDGWPB7NH0-AF
"""

import csv
import sys
from io import StringIO

def classify(cons):
    a1 = list()
    a2 = list()
    a3 = list()
    a4 = list()
    a5 = list()
    for con in cons:
        a1.append(con)
        a2.append(con[::-1])
        for other_con in [c for c in cons if c != con]:
            if con[1] == other_con[0]:
                a3.append([con[0], other_con[1]])
                a4.append([other_con[1], con[0]])
            elif con[0] == other_con[0]:
                a5.append([con[1], other_con[1]])
    return a1, a2, a3, a4, a5

def task(csv_str):
    csv_io = StringIO(csv_str)
    reader = csv.reader(csv_io)
    data = list(reader)
    classes = classify(data)
    result = []
    for c in classes:
      result.append([])
      for pair in c:
        result[-1].append(int(pair[0]))
      result[-1] = list(set(result[-1]))
    return result
