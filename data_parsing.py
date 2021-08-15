import sys
import re
from random import *
import sys
import pandas as pd
import numpy as np

CH_IDX = 16
DATA_IDX = 30
def script_formatting():
    sys.stdout = open('data.txt', 'w')

    for scan in range(30):
        for ch in range(16):
            print("variables[%d][%d] = %f" % (ch, scan, random()))

    sys.stdout.close()


def parse_data():
    f = open("data.txt")

    data = f.readlines()
    line_cnt = len(data)

    print(line_cnt)
    print("total lines : %d" % line_cnt)
    lst = []
    for idx in range(line_cnt):

        line = re.findall("\d+\.\d+", data[idx])
        lst.append(list(map(float, line)))
        print(lst[idx])

    s_lst = []
    t_lst = []
    print(line_cnt)
    idx = 0
    while idx <= line_cnt:
        temp_lst = []
        print(idx)
        if idx >= line_cnt:
            break
        for t_idx in range(CH_IDX):
            temp_lst.append(lst[idx+t_idx])
        idx += 16
        s_lst.append(temp_lst)
        t_lst = list(zip(*s_lst))
    print(t_lst)
    return t_lst

def save_data(t_lst):
    t_lst = parse_data()
    print(type(t_lst))
    arr_lst = np.asarray(t_lst)
    arr = np.squeeze(arr_lst, axis=2)
    print(arr.shape)
    dataframe = pd.DataFrame(arr)
    dataframe.to_csv("output.csv")


if __name__ == '__main__':
    lst = parse_data
    save_data(lst)
