#!/usr/bin/env python3

import os

from difflib import SequenceMatcher
from typing import List
from tabulate import tabulate


def main():

    preffix: str = "./genomas/"

    fileList: List[str] = os.listdir(preffix)

    rows: List[List[str]] = [[]]

    for i in range(len(fileList)):
        row: List[str] = [fileList[i]] + [""] * (i+1)

        file1 = open(preffix + fileList[i]).read()

        for j in range(i+1, len(fileList)):
            file2 = open(preffix + fileList[j]).read()

            m = SequenceMatcher(None, file1, file2)
            row.append("{:0.2f}%".format(m.ratio()*100))

        rows.append(row)

    print(tabulate(rows, headers=[""] + fileList))


if __name__ == "__main__":
    main()
