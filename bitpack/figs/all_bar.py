#! /usr/bin/env python3

import copy
import numpy as np
import numpy.linalg as nlin
import os, sys, math, re, statistics
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import statistics as st
import re

NETS=("Alexnet-BS16", "Alexnet-BS32", "Alexnet-BS64", "VGG-BS16", "VGG-BS32", 
    "VGG-BS64", "Resnet-BS32", "Resnet-BS64", "Resnet-BS128", "Average")

BASELINES=(1,1,1,1,1,1,1,1,1,1)
ADAPTIVES=[0.893, 0.934, 0.994, 0.927, 0.949, 0.871, 0.969, 0.956, 0.951]
ADAPTIVES.append(st.mean(ADAPTIVES))
ORACLES=[0.884, 0.89, 0.909, 0.918, 0.843, 0.853, 0.921, 0.857, 0.8537]
ORACLES.append(st.mean(ORACLES))

print(ADAPTIVES[-1])
print(ORACLES[-1])

VER=(BASELINES, ADAPTIVES, ORACLES)
VER_TAGS=("Baseline", "$A^2$DTWP", "Oracle")

#DATA=
#{
#    "Alexnet-BS16": {"baseline": 1, 
#                     "best": 0.884,
#                     "adaptive": 0.893
#                    },
#    "Alexnet-BS32": {"baseline": 1, 
#                     "best": 0.89,
#                     "adaptive": 0.934
#                    },
#    "Alexnet-BS64": {"baseline": 1, 
#                     "best": 0.909,
#                     "adaptive": 0.994
#                    },
#    "VGG-BS16": {"baseline": 1, 
#                     "best": 0.918,
#                     "adaptive": 0.927
#                    },
#    "VGG-BS32": {"baseline": 1, 
#                     "best": 0.843,
#                     "adaptive": 0.949
#                    },
#    "VGG-BS64": {"baseline": 1, 
#                     "best": 0.853,
#                     "adaptive": 0.871
#                    },
#    "Resnet-BS16": {"baseline": 1, 
#                     "best": 1,
#                     "adaptive": 1
#                    },
#    "Resnet-BS32": {"baseline": 1, 
#                     "best": 1,
#                     "adaptive": 1
#                    },
#    "Resnet-BS64": {"baseline": 1, 
#                     "best": 1,
#                     "adaptive": 1
#                    },
#    "ResnetBS128": {"baseline": 1, 
#                     "best": 1,
#                     "adaptive": 1
#                    },
#}

if __name__ == "__main__":
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True
    COLOR = ('0', '0.4', '0.8', '1')
    HATCH = (' ', 'ooo', '///' )

    bar_width = 0.14
    index = np.arange(len(NETS))
    pname = "all_bars.pdf"
    with PdfPages(pname) as pdf:
        fig = plt.figure()
        axes = fig.add_subplot(111)
        for iver, ver in enumerate(VER):
            axes.bar(index+bar_width*iver, ver, bar_width, alpha=1, 
                    label=VER_TAGS[iver], color='0.8', hatch=HATCH[iver], 
                    edgecolor='0')

        axes.set_xticks(index+bar_width)
        axes.set_ylabel("Normalized Elapse Time")
        axes.set_xticklabels(NETS, rotation=25, fontsize=8)
        axes.set_ylim(ymin=0.7)
        xleft, xright = axes.get_xlim()
        ybottom, ytop = axes.get_ylim()
        ratio = 0.3
        axes.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
        #axes.set_ylim([0.6,1.3])
        #plt.legend(loc=0, fontsize=10)
        plt.legend(bbox_to_anchor=(0.5, 1.20), loc=9, borderaxespad=0., fontsize=10, ncol=3) 
        pdf.savefig(dpi=100, bbox_inches='tight')
        plt.close()


    ### Power9
    BASELINES=(1,1,1,1,1,1,1,1,1,1)
    ADAPTIVES=[0.814, 0.858, 0.9, 0.718, 0.799, 0.889, 0.979, 0.931, 0.885]
    ADAPTIVES.append(st.mean(ADAPTIVES))
    ORACLES=[0.791, 0.832, 0.876, 0.709, 0.752, 0.86, 0.933, 0.889, 0.772]
    ORACLES.append(st.mean(ORACLES))
    VER=(BASELINES, ADAPTIVES, ORACLES)

    bar_width = 0.14
    index = np.arange(len(NETS))
    pname = "all_bars_p9.pdf"
    with PdfPages(pname) as pdf:
        fig = plt.figure()
        axes = fig.add_subplot(111)
        for iver, ver in enumerate(VER):
            axes.bar(index+bar_width*iver, ver, bar_width, alpha=1, 
                    label=VER_TAGS[iver], color='0.8', hatch=HATCH[iver], 
                    edgecolor='0')

        axes.set_xticks(index+bar_width)
        axes.set_ylabel("Normalized Elapse Time")
        axes.set_xticklabels(NETS, rotation=25, fontsize=8)
        axes.set_ylim(ymin=0.7)
        xleft, xright = axes.get_xlim()
        ybottom, ytop = axes.get_ylim()
        ratio = 0.3
        axes.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)
        #axes.set_ylim([0.6,1.3])
        #plt.legend(loc=0, fontsize=10)
        plt.legend(bbox_to_anchor=(0.5, 1.20), loc=9, borderaxespad=0., fontsize=10, ncol=3) 
        pdf.savefig(dpi=100, bbox_inches='tight')
        plt.close()

