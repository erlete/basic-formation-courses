import scipy as sc

img_r = sc.datasets.face().copy()
img_g = sc.datasets.face().copy()
img_b = sc.datasets.face().copy()


def splitter():

    for i in range(0, len(img_r)):
        for j in range(0, len(img_r[0])):
            for k in range(0, len(img_r[0][0])):
                match k:
                    case 0:
                        img_r[i][j][k] = img_r[i][j][0]
                        img_g[i][j][k] = 0
                        img_b[i][j][k] = 0
                    case 1:
                        img_r[i][j][k] = 0
                        img_g[i][j][k] = img_g[i][j][1]
                        img_b[i][j][k] = 0
                    case 2:
                        img_r[i][j][k] = 0
                        img_g[i][j][k] = 0
                        img_b[i][j][k] = img_b[i][j][2]

    colors = [img_r, img_g, img_b]
    return colors
