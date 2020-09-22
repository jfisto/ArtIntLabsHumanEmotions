__connections__ = {
    0: [1, 17, 36],
	1: [2, 36, 41],
	2: [3, 31, 41],
	3: [4, 31, 48],
	4: [5, 48],
	5: [6, 48, 59],
	6: [7, 58, 59],
	7: [8, 57, 58],
	8: [9, 57],
	9: [10, 56, 57],
	10: [11, 55, 56],
	11: [12, 55],
	12: [13, 54, 55],
	13: [14, 35, 54],
	14: [15, 35, 46],
	15: [16, 45, 46],
	16: [26, 45],
	17: [18, 36],
	18: [19, 36, 37],
	19: [20, 37],
	20: [21, 37, 38],
	21: [22, 27, 38, 39],
	22: [23, 27, 42, 43],
	23: [24, 43, 44],
	24: [25, 44],
	25: [26, 44, 45],
	26: [45],
	27: [28, 39, 42],
	28: [29, 39, 42],
	29: [30, 31, 35, 39, 40, 42, 47],
	30: [31, 32, 33, 34, 35],
	31: [32, 40, 41, 48, 49, 50],
	32: [33, 50, 51],
	33: [34, 51],
	34: [35, 51, 52],
	35: [46, 47, 52, 53, 54],
	36: [37, 41],
	37: [38],
	38: [39],
	39: [40],
	40: [41],
	41: [],
	42: [43, 47],
	43: [44],
	44: [45],
	45: [46],
	46: [47],
	47: [],
	48: [49, 59, 60],
	49: [50, 60, 61],
	50: [51, 61, 62],
	51: [52, 62],
	52: [53, 62, 63],
	53: [54, 63, 64],
	54: [55, 64],
	55: [56, 64, 65],
	56: [57, 65, 66],
	57: [58, 66],
	58: [59, 66, 67],
	59: [60, 67],
	60: [61, 67],
	61: [62],
	62: [63],
	63: [64],
	64: [65],
	65: [66],
	66: [67],
}

from ...dirs import DIR_DATA_NUMPY

if __name__ == '__main__':

    import numpy as np

    from pathlib import Path

    connections = []
    for i in __connections__.keys():
        for j in __connections__[i]:
            connections.append((i, j))

    connections = np.array(connections)
    outpath = DIR_DATA_NUMPY / 'biometry_connections.npy'
    np.save(outpath.as_posix(), connections)
