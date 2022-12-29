import numpy as np
import json

def to_json(s):
    js = json.loads(s)
    s = []
    for j in js:
        if isinstance(j, list):
            s.append(j)
        if isinstance(j, str):
            a = []
            a.append(j)
            s.append(a)
    return s

def exp_ind(arr, exps):
    t = -1
    for i in range(len(exps)):
        if arr == exps[i]:
            t = i
    return t

def create_matrix(exps, index):
    e = np.zeros((len(exps[index]), len(exps[index])))
    for i in range(len(exps[index])):
        for j in range(len(exps[index])):
            if exps[index][i] < exps[index][j]:
                e[i][j] = 1
            if exps[index][i] == exps[index][j]:
                e[i][j] = 0.5
            if exps[index][i] > exps[index][j]:
                e[i][j] = 0
    return e

def task(js):
    exps = to_json(js)
    exps_m = []
    for e in exps:
        exps_m.append(create_matrix(exps, exp_ind(e, exps)))
    m = np.zeros(exps_m[0].shape)
    for i in range(exps_m[0].shape[0]):
        for j in range(exps_m[0].shape[0]):
            for k in range(len(exps_m)):
                m[i][j] += 1/exps_m[k].shape[0] * exps_m[k][i][j]
    k0 = []
    for i in range(exps_m[0].shape[0]):
        k0.append(1/exps_m[0].shape[0])
    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k = np.dot(1/l, y)
    while max(abs(k-k0)) >= 0.001:
        k0 = k
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k = np.dot(1/l, y)
    return k