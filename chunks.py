import math


def chunks(img, n):
    """
    n = number of images 
    """
    shape = img.shape
    imgs = []

    nx = int(n * (shape[1]/(shape[0] + shape[1])))
    ny = n - nx

    x = int(shape[0]/n)
    y = int(shape[0]/n)

    for i in range(nx - 1):
        line = []
        for j in range(ny - 1):
            line.append(img[y*j: y*(j+1), x*i: x*(i+1), ::])
        imgs.append(line)
    return imgs


if __name__ == "__main__":
    import cv2

    res = chunks(cv2.imread('test.png'), 100)[30][30]
