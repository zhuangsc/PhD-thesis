#!/usr/bin/env python

import sys, glob, os
import re

VER = ("0_16", "1_24")
#BPE = 2002
#BPE = 1001

ELAPSE = [[] for ver in VER]
ELAPSE2 = [[] for ver in VER]
CELAPSE = []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: {} [dir]".format(sys.argv[0]))
        sys.exit(1)

    dir_name = os.path.abspath(sys.argv[1])
    BPE = int(sys.argv[2])
    for iver, ver in enumerate(VER):
        fnames0 = "*_*_{}_*.out".format(ver)
        fnames0 = os.path.join(dir_name, fnames0)
        fnames = sorted(glob.glob(fnames0))
        base_elapse = .0
        for lf, fname in enumerate(fnames):
            with open(fname, 'r') as f:
                for l, line in enumerate(f):
                    if re.search(r"\bstep\b", line):
                        ELAPSE[iver].append(float(line.split()[12])+base_elapse)
            base_elapse = ELAPSE[iver][-1]
    
    for iver, _ in enumerate(VER):
        for i in range(int(len(ELAPSE[iver])/BPE)):
            ELAPSE2[iver].append(ELAPSE[iver][(i+1)*BPE-1])

    if len(ELAPSE2[0]) <= len(ELAPSE2[1]):
        CELAPSE = [ELAPSE2[1][i]/ELAPSE2[0][i] for i in range(len(ELAPSE2[0]))]
    else:
        CELAPSE = [ELAPSE2[1][i]/ELAPSE2[0][i] for i in range(len(ELAPSE2[1]))]

    for i, e in enumerate(CELAPSE):
        print("'{}': {},".format(i+1, e))
    #print(CELAPSE)
