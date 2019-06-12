#!/usr/bin/env python

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def mk_groups(data):
    try:
        newdata = data.items()
    except:
        return

    thisgroup = []
    groups = []
    for key, value in newdata:
        newgroups = mk_groups(value)
        if newgroups is None:
            thisgroup.append((key, value))
        else:
            thisgroup.append((key, len(newgroups[-1])))
            if groups:
                groups = [g + n for n, g in zip(newgroups, groups)]
            else:
                groups = newgroups
    return [thisgroup] + groups

def add_line(ax, xpos, ypos):
    line = plt.Line2D([xpos, xpos], [ypos + .1, ypos],
                      transform=ax.transAxes, color='black')
    line.set_clip_on(False)
    ax.add_line(line)

def label_group_bar(ax, data):
    groups = mk_groups(data)
    xy = groups.pop()
    x, y = zip(*xy)
    ly = len(y)
    xticks = range(1, ly + 1)

    ax.bar(xticks, y, align='center', color='0.5', edgecolor='0', hatch=HATCH[2])
    ax.set_xticks(xticks)
    ax.set_xticklabels(x, fontsize=9, rotation=0)
    ax.set_ylabel("Normalized Elapse Time")
    ax.set_xlim(.5, ly + .5)
    ax.set_ylim(ymin=0.6)
    ax.yaxis.grid(True)
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ratio = 0.3
    ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

    scale = 1. / ly
    for pos in range(ly + 1):
        add_line(ax, pos * scale, -.1)
    ypos = -.2
    while groups:
        group = groups.pop()
        pos = 0
        for label, rpos in group:
            lxpos = (pos + .5 * rpos) * scale
            ax.text(lxpos, ypos, label, ha='center', transform=ax.transAxes, 
                    fontsize=9)
            add_line(ax, pos * scale, ypos)
            pos += rpos
        add_line(ax, pos * scale, ypos)
        ypos -= .1

if __name__ == '__main__':
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True
    plt.minorticks_off()
    COLOR = ('0', '0.4', '0.8', '1')
    HATCH = (' ', 'ooo', '///' )

    data = {
            'Alexnet-BS64': {
                    #'1': 0.980,
                    #'2': 0.987,
                    #'3': 0.992,
                    '4': 0.995,   ## FP-32 15.31%  A2DTWP 14.69%
                    #'5': 0.995,
                    #'6': 0.993,
                    #'7': 0.993,
                    '8': 0.992,   ## FP-32 25.23%  A2DTWP 28.71%
                    #'9': 0.992,
                    #'10': 0.992,
                    #'11': 0.991,
                    '12': 0.992,  ## FP-32 29.81%  A2DTWP 30.19%
                    #'13': 0.993,
                    #'14': 0.995,
                    #'15': 0.996,
                    '16': 0.996,  ## FP-32 32.51%  A2DTWP 31.09%
                    #'17': 0.998,
                    #'18': 0.998,
                    #'19': 0.998,
                    '20': 0.990,  ## FP-32 39.21%  A2DTWP 41.31%
               },
            'VGG-BS64': {
                    #'1': 0.918,
                    '2': 0.907,   ## FP-32 11.96%  A2DTWP 10.13%
                    #'3': 0.911,
                    '4': 0.920,   ## FP-32 35.98%  A2DTWP 32.88%
                    #'5': 0.928,
                    '6': 0.936,   ## FP-32 43.54%  A2DTWP 44.01%
                    #'7': 0.931,
                    '8': 0.932,   ## FP-32 53.82%  A2DTWP 53.11%
               },
             'Resnet-BS128': {
                    #'1': 0.762,
                    #'2': 0.763,
                    #'3': 0.764,
                    '4': 0.765,   ## FP-32 25.81%  A2DTWP 22.81%
                    #'5': 0.763,
                    #'6': 0.764,
                    #'7': 0.767,
                    '8': 0.770,   ## FP-32 38.93%  A2DTWP 37.61%
                    #'9': 0.773,
                    #'10': 0.775,
                    #'11': 0.776,
                    '12': 0.778,  ## FP-32 45.13%  A2DTWP 46.81%
                    #'13': 0.777,
                    #'14': 0.777,
                    #'15': 0.777,
                    '16': 0.777,  ## FP-32 53.74%  A2DTWP 51.98%
                    #'17': 0.777,
                    #'18': 0.776,
               },
           }
    pname = "imagenet-1k-3net.pdf"
    with PdfPages(pname) as pdf:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        label_group_bar(ax, data)
        fig.subplots_adjust(bottom=0.3)
        pdf.savefig(dpi=100, bbox_inches='tight')
        plt.close()

    #data = {
    #        'Alexnet-BS64':
    #           {'x86':
    #               {'1': 0.980,
    #                '2': 0.987,
    #                '3': 0.992,
    #                '4': 0.995,
    #                '5': 0.995,
    #                '6': 0.993,
    #                '7': 0.993,
    #                '8': 0.992,
    #                '9': 0.992,
    #                '10': 0.992,
    #                '11': 0.991,
    #                '12': 0.992,
    #                '13': 0.993,
    #                '14': 0.995,
    #                '15': 0.996,
    #                '16': 0.996,
    #                '17': 0.998,
    #                '18': 0.998,
    #                '19': 0.998,
    #                },
    #            #'POWER9':
    #            #   {'1': 0.796,
    #            #    '2': 0.799,
    #            #    '3': 0.801,
    #            #    '4': 0.793,
    #            #    '5': 0.788,
    #            #    '6': 0.759,
    #            #    '7': 0.761,
    #            #    '8': 0.778,
    #            #    '9': 0.798,
    #            #    '10': 0.792,
    #            #    '11': 0.791,
    #            #    '12': 0.792,
    #            #    '13': 0.793,
    #            #    '14': 0.795,
    #            #    '15': 0.796,
    #            #    '16': 0.781,
    #            #    },
    #           },
    #        'VGG-BS64':
    #           {'x86':
    #               {'1': 0.918,
    #                '2': 0.907,
    #                '3': 0.911,
    #                '4': 0.920,
    #                '5': 0.928,
    #                '6': 0.936,
    #                '7': 0.931,
    #                },
    #            #'POWER9':
    #            #   {'1': 1.202,
    #            #    '2': 1.183,
    #            #    '3': 1.211,
    #            #    '4': 1.217,
    #            #    '5': 1.249,
    #            #    '6': 1.285,
    #            #    '7': 1.266,
    #            #    '8': 1.270,
    #            #    '9': 1.265,
    #            #    },
    #           },
    #         'Resnet-BS128':
    #           {'x86':
    #               {'1': 0.762,
    #                '2': 0.763,
    #                '3': 0.764,
    #                '4': 0.765,
    #                '5': 0.763,
    #                '6': 0.764,
    #                '7': 0.767,
    #                '8': 0.770,
    #                '9': 0.773,
    #                '10': 0.775,
    #                '11': 0.776,
    #                '12': 0.778,
    #                '13': 0.777,
    #                '14': 0.777,
    #                },
    #            #'POWER9':
    #            #   {'1': 1.201,
    #            #    '2': 1.204,
    #            #    '3': 1.260,
    #            #    '4': 1.300,
    #            #    '5': 1.341,
    #            #    '6': 1.298,
    #            #    '7': 1.292,
    #            #    },
    #           },
    #       }
