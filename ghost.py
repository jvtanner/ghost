#!/usr/bin/env python3

"""
Stanford CS106A Ghost Project
"""

import os
import sys
import math

# This line imports SimpleImage for use here
# This depends on the Pillow package
from simpleimage import SimpleImage


def pix_dist2(pix1, pix2):
    """
    Returns the square of the color distance between 2 pix tuples.
    >>> pix_dist2((1, 1, 1), (250, 250, 250))
    186003
    >>> pix_dist2((1, 1, 1), (100, 250, 0))
    71803
    >>> pix_dist2((1, 1, 1), (1, 1, 1))
    0
    """

    x_difference = abs(pix1[0] - pix2[0])
    y_difference = abs(pix1[1] - pix2[1])
    z_difference = abs(pix1[2] - pix2[2])
    return x_difference ** 2 + y_difference ** 2 + z_difference ** 2


def pix_avg(pixs):
    """
    When given a list of pixels, each with r, b, and g values,
    returns the avg values as one 'average pixel'
    >>> pix_avg([(1, 1, 1), (1, 1, 1), (28, 43, 58)])
    [10, 15, 20]
    >>> pix_avg([(0, 0, 40), (0, 40, 0), (40, 0, 0), (4, 4, 4)])
    [11, 11, 11]
    """
    total_red = 0
    total_blue = 0
    total_green = 0
    for pix in pixs:
        total_red += pix[0]
        total_blue += pix[2]
        total_green += pix[1]

    avg_red = total_red // len(pixs)
    avg_blue = total_blue // len(pixs)
    avg_green = total_green // len(pixs)

    return [avg_red, avg_blue, avg_green]


def best_pix(pixs):
    """
    Given a list of 3 or more pix, returns the best pix.
    >>> best_pix([(2, 2, 2), (2, 3, 4), (20, 20, 20)])
    (2, 3, 4)
    >>> best_pix([(0, 0, 0), (250, 250, 250), (100, 100, 100)])
    (100, 100, 100)
    >>> best_pix([(2, 2, 2), (2, 2, 2), (20, 20, 20)])
    (2, 2, 2)
    >>> best_pix([(2, 2, 2), (2, 3, 4), (20, 20, 20), (250, 250, 250)])
    (20, 20, 20)
    """
    # Get average of pixs (helper)
    avg = pix_avg(pixs)

    # Pick the pix whose distance to the avg is minimum (utilize Lambda)
    return min(pixs, key=lambda close: (pix_dist2(close, avg)))


def solve(images):
    """
    Given a list of image objects, compute and show
    a Ghost solution image based on these images.
    There will be at least 3 images and they will all be
    the same size.
    """
    solution = SimpleImage.blank(images[0].width, images[0].height)

    for x in range(images[0].width):
        for y in range(images[0].height):
            combo = []
            for i in range(len(images)):
                pix = images[i].get_pix(x, y)
                combo.append(pix)
            best = best_pix(combo)
            solution.set_pix(x, y, best)
    solution.show()


def jpgs_in_dir(dir):
    """
    (provided)
    Given the name of a directory
    returns a list of the .jpg filenames within it.
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided)
    Given a directory name, reads all the .jpg files
    within it into memory and returns them in a list.
    Prints the filenames out as it goes.
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print(filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    if len(args) == 1:
        images = load_images(args[0])
        solve(images)


if __name__ == '__main__':
    main()
